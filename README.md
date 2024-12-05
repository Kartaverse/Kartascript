# Kartascript v0.1 

Updated 2024-12-05 7.22 PM  
By Andrew Hazelden <andrew@andrewhazelden.com>  

Kartascript is a Python module for immersive post-production workflow automation. It provides PTGui .pts JSON file parsing tools.

## Open-Source License

- LGPL

## Dev Todo List:

- Add an interactive TUI (text user interface)
- Add the following functions:
	- GetOutputFilename

## Python Module Usage Examples

## Navigate into the folder where the Python module exists:

	cd $HOME/Desktop/kartascript/
	python3

## Open a PTS File:

	import kartascript as ks
	pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
	print(ks.Dump(pt))

## Open PTS from a URL:

	import kartascript as ks
	pt = ks.ReadURL("https://raw.githubusercontent.com/Kartaverse/Kartascript/refs/heads/master/Demo%20PT/Samyang_8mm_v001.pts")
	print(ks.Dump(pt))

## Count the number of lenses:

	import kartascript as ks
	pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
	lnum = ks.GetLensCount(pt)
	print(lnum)

## Count the number of images:

	import kartascript as ks
	pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
	inum = ks.GetImageCount(pt)
	print(inum)

## Read all of the image filenames:

	import kartascript as ks
	pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
	imglist = ks.GetImageFilenameList(pt)
	print(ks.Dump(imglist))

## Read an image filename:

	import kartascript as ks
	pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
	img = ks.GetImageFilename(pt,0)
	print(img)

## Write the include/exclude image mask to disk as a PNG image:

	import kartascript as ks
	pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
	index = 1
	print(ks.GetMaskImage(pt, index, "Demo PT/image.png"))

## Read an include/exclude image mask as Base64 encoded data:

	import kartascript as ks
	pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
	index = 1
	maskb64 = ks.GetMaskImageBase64(pt, 1)
	print(maskb64)

## Read the image dimensions:

	import kartascript as ks
	pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
	index = 0
	w, h = ks.GetImageSize(pt, index)
	print(w, h)

## Read the image yaw/pitch/roll rotations:

	import kartascript as ks
	pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
	index = 0
	x, y, z = ks.GetRotation(pt, index)
	print(x, y, z)

## Read the focal length for a single lens:

	import kartascript as ks
	pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
	index = 0
	focallength = ks.GetFocalLength(pt, index)
	print(focallength)

## Read the focal length for all the lenses:

	import kartascript as ks
	pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
	for index in range (ks.GetImageCount(pt)):
		focallength = ks.GetFocalLength(pt, index)
		print(focallength)

## Read the lens projection for a single image:

	import kartascript as ks
	pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
	index = 0
	projection = ks.GetLensProjection(pt, index)
	print(projection)

## Read the lens distortion ABC values for a single image:

	import kartascript as ks
	pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
	index = 0
	a, b, c = ks.GetLensABC(pt, index)
	print(a, b, c)

## Read the lens data for a single image:

	import kartascript as ks
	pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
	index = 0
	projection, focallength, shiftlongside, shiftshortside, hshear, vshear, a, b, c = ks.GetLenses(pt, index)
	print(projection, focallength, shiftlongside, shiftshortside, hshear, vshear, a, b, c)

## Read the lens data for all of the images:

	pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
	for index in range (ks.GetImageCount(pt)):
		projection, focallength, shiftlongside, shiftshortside, hshear, vshear, a, b, c = ks.GetLenses(pt, index)
		print(projection, focallength, shiftlongside, shiftshortside, hshear, vshear, a, b, c)

## Generate a CSV (comma-separated-value) spreadsheet of common image parameters to a string:

	import kartascript as ks
	pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
	csv_string = ks.GetCSVString(pt)
	print(csv_string)

## Generate a CSV (comma-separated-value) spreadsheet of common image parameters to a file on disk:

	import kartascript as ks
	pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
	print(ks.GetCSVFile(pt, "Demo PT/Under the Bridge PTGui v12.csv"))
