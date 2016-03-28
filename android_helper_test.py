#!/usr/bin/env python
# -*- coding: utf-8 -*-

from android_helper import *

if __name__ == "__main__":
    dp = 48
    print "Given %ddp, what are the px values from mdpi to xxxhdpi?" % dp
    print get_px_values_all_densities(dp)
    print ""

    test_dir = (os.getcwd() + os.path.sep + "test-dirs" +
                os.path.sep + "android" + os.path.sep + "helper")
    current_dirs = os.listdir(test_dir)
    if len(current_dirs) != 0:
        print "Note: %s already contains some dirs\n" % test_dir

    print "Making drawable directories"
    make_density_dirs(test_dir, True)
    print "Directories in output:", os.listdir(test_dir)
    print ""

    print "Making mipmap directories"
    make_density_dirs(test_dir, False)
    print "Directories in output:", os.listdir(test_dir)
    print ""
