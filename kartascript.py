"""
Kartascript v0.1 Updated 2024-12-03 8.24 AM
By Andrew Hazelden <andrew@andrewhazelden.com>

Kartascript is a Python module for immersive post-production workflow automation. It supports PTGui .pts JSON file parsing.

# Open-Source License
- LGPL

# Dev Todo List:
- Add an interactive TUI (text user interface)
- Add the following functions:
	- GetOutputFilename
	- GetLensProjection
	- GetFocalLength
	- GetLensABC
	- GetLensCount

# Python Module Usage Examples

# Navigate into the folder where the Python module exists:
cd $HOME/Desktop/kartascript/
python3

# Open a PTS File:
import kartascript as ks
pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
print(ks.Dump(pt))

# Open PTS from a URL:
import kartascript as ks
pt = ks.ReadURL("https://gitlab.com/WeSuckLess/Reactor/-/raw/master/Atoms/com.AndrewHazelden.KartaVP.PT/Comps/Kartaverse/PT/Demo%20PT/Samyang_8mm_v001.pts?ref_type=heads")
print(ks.Dump(pt))

# Count the number of images:
import kartascript as ks
pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
print(ks.GetImageCount(pt))

# Read all of the image filenames:
import kartascript as ks
pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
print(ks.Dump(ks.GetImageFilenameList(pt)))

# Read an image filename:
import kartascript as ks
pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
print(ks.GetImageFilename(pt,0))

# Write the include/exclude image mask to disk as a PNG image:
import kartascript as ks
pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
print(GetMaskImage(pt, 1,"Demo PT/image.png"))

# Read an include/exclude image mask as Base64 encoded data:
import kartascript as ks
pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
print(ks.GetMaskImageBase64(pt,0))

# Read the image dimensions:
import kartascript as ks
pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
print(ks.GetImageSize(pt,0))

# Read the image yaw/pitch/roll rotations:
import kartascript as ks
pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
print(ks.GetRotation(pt, 0))

# Generate a CSV (comma-separated-value) spreadsheet of common image parameters:
import kartascript as ks
pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
print(ks.GetCSV(pt))


"""
import json, os, sys, re, base64
from urllib.request import urlopen

def ReadFile(json_file):
	"""Load a pts JSON file from disk"""
	with open(json_file, encoding="UTF-8") as fh:
		data = json.load(fh)
		return data

def ReadString(json_string):
	"""Load a pts JSON string"""
	data = json.loads(json_string)
	return data
	
def ReadURL(url):
	"""Download an internet URL that points to pts JSON data"""
	html = urlopen(url)
	response = html.read().decode("UTF-8")
	data = json.loads(response)
	return data

def Dump(data):
	"""Dump the pts JSON data as formatted text"""
	return json.dumps(data, indent=4, ensure_ascii=True)

def GetImageCount(data):
	"""How many images are in the pts file? Returns the image count as a number."""
	if type(data) == dict:
		return len(data["project"]["imagegroups"])
	else:
		return None

def GetImageSize(data, inum):
	"""What are the dimensions of a specific image in the pts file? Returns the image width/height values as a list."""
	if type(data) == dict and type(inum) == int:
		return data["project"]["imagegroups"][inum]["size"]
	else:
		return None

def GetImageFilename(data, inum):
	"""What is the filename for a specific image in the pts file? Returns a relative image filename string."""
	if type(data) == dict and type(inum) == int:
		filename = data["project"]["imagegroups"][inum]["images"][0]["filename"]
		include = data["project"]["imagegroups"][inum]["images"][0]["include"]
		return filename, include
	else:
		return None

def GetImageFilenameList(data):
	"""What is are the filenames the images in a pts file? Returns a list of relative image filenames."""
	if type(data) == dict:
		filenames = []
		for index in range (len(data["project"]["imagegroups"])):
			filenames.append(data["project"]["imagegroups"][index]["images"][0]["filename"])
		return filenames
	else:
		return None

def GetMaskImageBase64(data, inum):
	"""Is there a mask for an image in a pts file? Returns a base64 encoded PNG format mask image."""
	if type(data) == dict:
		maskbitmapID = data["project"]["imagegroups"][inum]["maskbitmap"]
		if maskbitmapID != None:
			for index in range (len(data["assets"])):
				if data["assets"][index]["id"] == maskbitmapID:
					maskBase64 = data["assets"][index]["data"]
					return maskBase64
	return None

def GetMaskImage(data, inum, file):
	"""Is there a mask for an image in a pts file? Returns a PNG format mask image."""
	if type(data) == dict:
		maskbitmapID = data["project"]["imagegroups"][inum]["maskbitmap"]
		if maskbitmapID != None:
			for index in range (len(data["assets"])):
				if data["assets"][index]["id"] == maskbitmapID:
					maskBase64 = data["assets"][index]["data"]
					maskImage = base64.b64decode(maskBase64)
					with open(file, "wb") as pngFile:
						pngFile.write(maskImage)
						return file
	return None

def GetRotation(data, inum):
	"""What is are the rotation values for an image in a pts file? Returns a list with yaw/pitch/roll values."""
	rotation = []
	if type(data) == dict:
		rotation.append(data["project"]["imagegroups"][inum]["position"]["params"]["yaw"])
		rotation.append(data["project"]["imagegroups"][inum]["position"]["params"]["pitch"])
		rotation.append(data["project"]["imagegroups"][inum]["position"]["params"]["roll"])
		return rotation
	else:
		return None

def GetCSV(data):
	totalImages = GetImageCount(data)
	csv_string = "Filename,Include,Image Width,Image Height,X Rotation,Y Rotation,Z Rotation\n"
	for index in range (totalImages):
		filename, include = GetImageFilename(data, index)
		width, height = GetImageSize(data, index)
		x, y, z = GetRotation(data, index)
		csv_string += str(filename) + "," + str(include) + "," + str(width) + "," + str(height) + "," + str(x) + "," + str(y) + "," +  str(z) + "\n"
	return csv_string

if __name__ == '__main__':
	print("\nKartascript -- v0.1 Copyright (C) 2024 Andrew Hazelden.")
	print("---------------------------------------------------------\n")
	print("A Python module for immersive post-production workflow automation. It supports PTGui .pts JSON file parsing.\n\n")

	pt = ReadURL("https://gitlab.com/WeSuckLess/Reactor/-/raw/master/Atoms/com.AndrewHazelden.KartaVP.PT/Comps/Kartaverse/PT/Demo%20PT/Samyang_8mm_v001.pts?ref_type=heads")

	print(GetCSV(pt))