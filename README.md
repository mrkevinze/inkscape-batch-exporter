# Inkscape Batch Exporter

## Introduction
A Python script which exports all Inkscape svg files in a given directory to png files. This utility negates the need to manually export each svg using the Inkscape GUI, thus freeing up valuable time for more creative work.

This script was designed with Android developers in mind, who need to make multiple density-specific (mdpi to xxxhdpi) png files from a single svg.

## Notes
1. Compatible with Python 2.7. 
2. The export area is the page in the svg. If you need to customize this behavior, look up the `build_command_list` function within `exporter.py`.
3. A batch export option for iOS developers will be a good extension.

## Usage

### Simple Example
1. Drag your svg files to a clone of this repo.
2. Open your command line and cd to this repo.
3. If your Inkscape program is in the usual installation directory, running  
`python exporter.py <width>` should work; replace `<width>` with a suitable number.
4. View the output png files in the same directory.

### Typical Usage
Dragging your svg files into the repo would unnecessarily pollute the repo and disrupt your existing project workspace or setup. You should specify the input and output directories with additional command line options, such as

`python exporter.py -i <input_dir> -o <output_dir> <width>`

Also, if you are an Android developer, specify `-a True` to generate density-specific png files.

### Usage Details
To view usage details, run `python exporter.py -h`.
You will see something like this:

```
usage: exporter.py [-h] [-inkscape INKSCAPE_PATH] [-i INPUT_DIR]
                   [-o OUTPUT_DIR] [-height HEIGHT] [-a IS_ANDROID]
                   [-d IS_DRAWABLE] [-v IS_VERBOSE]
                   width

positional arguments:
  width                 width of the exported pngs (in Android dp if
                        IS_ANDROID is True, in px otherwise)

  (If the script is unable to find Inkscape program at the default path,
  then INKSCAPE_PATH will be a mandatory positional argument instead.)

optional arguments:
  -h, --help            show this help message and exit
  -inkscape INKSCAPE_PATH
                        path to your Inkscape program, defaults to
                        <an_os_specific_path>
  -i INPUT_DIR          path to the dir containing your svg(s), defaults to
                        <the_current_working_dir>
  -o OUTPUT_DIR         path to the dir that will contain the output, defaults
                        to <the_current_working_dir>
  -height HEIGHT        height of the exported pngs (in Android dp if
                        IS_ANDROID is True, in px otherwise), defaults to None
                        which lets Inkscape automatically compute the height
                        based on the aspect ratio of the svg
  -a IS_ANDROID         specify whether the script should create different
                        outputs for each Android display density, defaults to
                        False
  -d IS_DRAWABLE        specify whether the output directories are for Android
                        drawable or mipmap images, defaults to True; ignore
                        this if IS_ANDROID is False
  -v IS_VERBOSE         enable to view shell output, defaults to True
```

## License
Please see LICENSE.txt.
