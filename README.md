# Kartascript v0.1 

Updated 2024-12-03 8.24 AM  
By Andrew Hazelden <andrew@andrewhazelden.com>  

Kartascript is a Python module for immersive post-production workflow automation. It supports PTGui .pts JSON file parsing.

## Open-Source License
- LGPL

## Dev Todo List:
- Add an interactive TUI (text user interface)
- Add the following functions:
	- GetOutputFilename
	- GetLensProjection
	- GetFocalLength
	- GetLensABC
	- GetLensCount

## Python Module Usage Examples

	# Navigate into the folder where the Python module exists and launch a Python interactive session using a terminal program:
	cd $HOME/Desktop/kartascript/
	python3

## Open a PTS File:

	import kartascript as ks
	pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
	print(ks.Dump(pt))

## Open PTS from a URL:

	import kartascript as ks
	pt = ks.ReadURL("https://gitlab.com/WeSuckLess/Reactor/-/raw/master/Atoms/com.AndrewHazelden.KartaVP.PT/Comps/Kartaverse/PT/Demo%20PT/Samyang_8mm_v001.pts?ref_type=heads")
	print(ks.Dump(pt))

## Count the number of images:

	import kartascript as ks
	pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
	print(ks.GetImageCount(pt))

## Read all of the image filenames:

	import kartascript as ks
	pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
	print(ks.Dump(ks.GetImageFilenameList(pt)))

## Read an image filename:

	import kartascript as ks
	pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
	print(ks.GetImageFilename(pt,0))

## Write the include/exclude image mask to disk as a PNG image:

	import kartascript as ks
	pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
	print(ks.GetMaskImage(pt, 1,"Demo PT/image.png"))

## Read an include/exclude image mask as Base64 encoded data:

	import kartascript as ks
	pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
	print(ks.GetMaskImageBase64(pt,0))

## Read the image dimensions:

	import kartascript as ks
	pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
	print(ks.GetImageSize(pt,0))

## Read the image yaw/pitch/roll rotations:

	import kartascript as ks
	pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
	print(ks.GetRotation(pt, 0))

## Generate a CSV (comma-separated-value) formatted spreadsheet of common image parameters:

	import kartascript as ks
	pt = ks.ReadFile("Demo PT/Under the Bridge PTGui v12.pts")
	print(ks.GetCSV(pt))

