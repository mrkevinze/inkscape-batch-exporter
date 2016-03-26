#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test scripts; requires inspection of the print logs and file output.
See exporter_test_log.txt."""

from exporter import *

if __name__ == "__main__":
    sep = os.path.sep
    input_dir = "test-dirs" + sep + "input"

    android_dir = "test-dirs" + sep + "android"
    drawable_dir = android_dir + sep + "drawable"
    mipmap_dir = android_dir + sep + "mipmap"

    regular = "test-dirs" + sep + "regular"
    height_auto_dir = regular + sep + "height-auto"
    height_dir = regular + sep + "height"

    for svg_path in get_svg_paths(input_dir):
        print "svg_path:", svg_path
        print "svg_name:", get_svg_name(svg_path)
        print "png_path:", get_png_path(regular, get_svg_name(svg_path))
        print ""

    inkscape_path = get_default_inkscape_path()
    print "Inkscape path:", inkscape_path

    print "\n===Test export_svgs===\n"

    print "Export with height specified; see %s\n" % height_dir
    export_svgs(inkscape_path, input_dir, height_dir, 48, 36)

    print "Export using auto-height; see %s\n" % height_auto_dir
    export_svgs(inkscape_path, input_dir, height_auto_dir, 48, None)

    print "===Test export_svgs_android_densities===\n"

    print "Export drawable with height specified; see %s\n" % drawable_dir
    export_svgs_android_densities(inkscape_path,
                                  input_dir, drawable_dir,
                                  True, 24, 18)

    print "Export mipmap using auto-height; see %s\n" % mipmap_dir
    export_svgs_android_densities(inkscape_path,
                                  input_dir,
                                  mipmap_dir,
                                  False, 24, None)

    print "===Test command line invocations===\n"
    cmd1 = ("python exporter.py -i test-dirs/input " +
            "-o test-dirs/cmd/cmd1 " +
            "-height 36 -a True -d True -v True 48")

    cmd2 = ("python exporter.py -i test-dirs/input " +
            "-o test-dirs/cmd/cmd2 " +
            "-inkscape \"C:\\Program Files\\Inkscape\\inkscape.exe\" " +
            "-a True -d False -v False 48")

    cmd3 = ("python exporter.py -i test-dirs/input " +
            "-o test-dirs/cmd/cmd3 " +
            "-a True 48")

    cmd4 = ("python exporter.py -i test-dirs/input " +
            "-o test-dirs/cmd/cmd4 " +
            "-a False 48")

    cmd5 = ("python exporter.py -i test-dirs/input " +
            "-o test-dirs/cmd/cmd5 -height 36 48")

    cmd6 = "python exporter.py 48"

    cmd_list = [cmd1, cmd2, cmd3, cmd4, cmd5, cmd6]
    for cmd in cmd_list:
        print cmd
        os.system(cmd)
        print "===\n"
