#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test scripts; requires inspection of the print logs and file output.
See exporter_test_log.txt."""

from exporter import *

if __name__ == "__main__":
    sep = os.path.sep
    input_dir = "test-dirs" + sep + "input"

    vanilla_dir = "test-dirs" + sep + "vanilla"
    width_only_dir = vanilla_dir + sep + "width-only"
    height_only_dir = vanilla_dir + sep + "height-only"
    both_w_and_h_dir = vanilla_dir + sep + "both"
    neither_dir = vanilla_dir + sep + "neither"

    android_dir = "test-dirs" + sep + "android"
    drawable_width_only_dir = android_dir + sep + "drawable-width-only"
    mipmap_height_only_dir = android_dir + sep + "mipmap-height-only"
    mipmap_both_dir = android_dir + sep + "mipmap-both"
    drawable_neither_dir = android_dir + sep + "drawable-neither"

    print "\n===Basic path calculations===\n"
    for svg_path in get_svg_paths(input_dir):
        print "svg_path:", svg_path
        print "svg_name:", get_svg_name(svg_path)
        print "png_path:", get_png_path(vanilla_dir, get_svg_name(svg_path))
        print "dimens:", get_dimens(svg_path)
        print ""

    inkscape_path = get_default_inkscape_path()
    print "Inkscape path:", inkscape_path

    print "\n===Test export_svgs===\n"

    print "Export with only width specified; see %s\n" % width_only_dir
    export_svgs(inkscape_path, input_dir, width_only_dir, 12, None)

    print "Export with only height specified; see %s\n" % height_only_dir
    export_svgs(inkscape_path, input_dir, height_only_dir, None, 12)

    print ("Export with both width and height specified; see %s\n" %
           both_w_and_h_dir)
    export_svgs(inkscape_path, input_dir, both_w_and_h_dir, 12, 16)

    print ("Export with neither height nor width specified; see %s\n" %
           neither_dir)
    export_svgs(inkscape_path, input_dir, neither_dir, None, None)

    print "===Test export_svgs_for_android===\n"

    print ("Export drawable with only width specified; see %s\n" %
           drawable_width_only_dir)

    export_svgs_for_android(inkscape_path, input_dir,
                            drawable_width_only_dir,
                            True, 24, None)

    print ("Export mipmap with only height specified; see %s\n" %
           mipmap_height_only_dir)

    export_svgs_for_android(inkscape_path, input_dir,
                            mipmap_height_only_dir,
                            False, None, 24)

    print "Export mipmap with both specified; see %s\n" % mipmap_both_dir

    export_svgs_for_android(inkscape_path, input_dir,
                            mipmap_both_dir,
                            False, 24, 24)

    print ("Export drawable with neither specified; see %s\n" %
           drawable_neither_dir)

    export_svgs_for_android(inkscape_path, input_dir,
                            drawable_neither_dir,
                            True, None, None)

    print "===Test command line invocations===\n"

    cmd1 = ("python exporter.py -i test-dirs/input " +
            "-o test-dirs/cmd/cmd1 -width 12 " +
            "-height 36 -a True -d True -v True")

    cmd2 = ("python exporter.py -i test-dirs/input " +
            "-o test-dirs/cmd/cmd2 -width 12 " +
            "-inkscape \"C:\\Program Files\\Inkscape\\inkscape.exe\" " +
            "-a True -d False -v False")

    cmd3 = ("python exporter.py -i test-dirs/input " +
            "-o test-dirs/cmd/cmd3 -height 12 -a True")

    cmd4 = ("python exporter.py -i test-dirs/input " +
            "-o test-dirs/cmd/cmd4 -a True")

    cmd5 = ("python exporter.py -i test-dirs/input " +
            "-o test-dirs/cmd/cmd5 " +
            "-a False -width 12 -height 36")

    cmd6 = ("python exporter.py -i test-dirs/input " +
            "-o test-dirs/cmd/cmd6 -width 12")

    cmd7 = ("python exporter.py -i test-dirs/input " +
            "-o test-dirs/cmd/cmd7 -height 12")

    cmd8 = ("python exporter.py -i test-dirs/input " +
            "-o test-dirs/cmd/cmd8")

    cmd9 = "python exporter.py"

    cmd_list = [cmd1, cmd2, cmd3, cmd4, cmd5, cmd6, cmd7, cmd8, cmd9]
    for cmd in cmd_list:
        print cmd
        os.system(cmd)
        print "===\n"
