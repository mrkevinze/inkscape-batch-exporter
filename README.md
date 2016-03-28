# Inkscape Batch Exporter

## Introduction
A Python script which exports all Inkscape svg files in a given directory to png files. This utility negates the need to manually export each svg using the Inkscape GUI, thus freeing up valuable time for more creative work.

## Notes
1. Compatible with Python 2.7. 
2. The export area is the page in the svg. If you need to customize this behavior, look up the `build_command_list` function within `exporter.py`.
3. A batch export option for iOS developers will be a good extension.

## Usage

### Simple Example
1. Drag your svg files to a clone of this repository.
2. Open your command line and cd to this repository.
3. Run `python exporter.py`.
4. View the output png files in the repository.

### Typical Usage Example
Dragging your svg files into the repository is generally a bad idea as it disrupts your existing project setup. You should specify the input and output directories with additional command line options, such as

`python exporter.py -i <input_dir> -o <output_dir>`

Notice that the input and output are directories (folders) and not individual files. After all, this is a batch exporter script.

Also, if you are an Android developer, specify `-a True` to generate density-specific png files.

### About Width and Height
By default, the width and height values are determined from the document page width and height of each Inkscape svg.

However, if you override the default behavior by specifying `-width` or `-height`, all outputs would share the same width or height.

Moreover, if `-a True` is specified, the width and height will be treated as Android dp values; the dp values will be used to calculate the actual pixel width and height of the output at each display density. For example, a 48dp value is 48px at mdpi and 192px at xxxhdpi.



### Full Usage Details
To view all the usage details, run `python exporter.py -h`.
You will see something like this:

```
usage: exporter.py [-h] [-inkscape INKSCAPE_PATH] [-i INPUT_DIR]
                   [-o OUTPUT_DIR] [-width WIDTH] [-height HEIGHT]
                   [-a IS_ANDROID] [-d IS_DRAWABLE] [-v IS_VERBOSE]

positional arguments:
  None, but if the script is unable to find the Inkscape program at the default
  path, then INKSCAPE_PATH will be a mandatory positional argument.

optional arguments:
  -h, --help            show this help message and exit
  -inkscape INKSCAPE_PATH
                        path to your Inkscape program, defaults to
                        <an_os_specific_path>
  -i INPUT_DIR          path to the dir containing your svg(s), defaults to
                        <the_current_working_dir>
  -o OUTPUT_DIR         path to the dir that will contain the output, defaults
                        to <the_current_working_dir>
  -width WIDTH          sets the integer width of all exported pngs (in
                        Android dp if IS_ANDROID, in px otherwise), defaults
                        to the document page width in px set in each input svg
                        file
  -height HEIGHT        same as width, but for height instead
  -a IS_ANDROID         specify whether the script should create different
                        outputs for each Android display density, defaults to
                        False
  -d IS_DRAWABLE        specify whether the output directories are for Android
                        drawable or mipmap images, defaults to True; ignore
                        this if IS_ANDROID is False
  -v IS_VERBOSE         enable to view shell output, defaults to True

```

## License
MIT License

Copyright (c) 2016 Kevin Lee

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
