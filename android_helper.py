#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Contains functions that handle different Android densities."""

import os
import errno

DENSITIES = ("mdpi", "hdpi", "xhdpi", "xxhdpi", "xxxhdpi")
PX_MULTIPLIERS = (1, 1.5, 2, 3, 4)


def get_px_values_all_densities(dp):
    assert len(DENSITIES) == len(PX_MULTIPLIERS)

    px_values = []
    for i in xrange(len(DENSITIES)):
        px_values.append(int(round((PX_MULTIPLIERS[i] * dp))))
    return px_values


def make_density_dirs(parent_dir, is_drawable):
    for density in DENSITIES:
        child_dir = get_child_dir(parent_dir, is_drawable, density)
        make_dir_if_doesnt_exist(child_dir)


def make_dir_if_doesnt_exist(dir_path):
    try:
        os.makedirs(dir_path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def get_child_dir(parent_dir, is_drawable, density):
    prefix = get_dir_prefix(is_drawable)
    return parent_dir + os.path.sep + prefix + density


def get_dir_prefix(is_drawable):
    if is_drawable:
        return "drawable-"
    else:
        # Note: mipmap directories are reserved for app icons only.
        return "mipmap-"
