#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""As this is the main module of the project, please see README.md."""

import os
import argparse
import subprocess

import android_helper

verbose = True


def export_svgs_android_densities(inkscape_path, input_dir, output_dir,
                                  is_drawable, width_dp, height_dp):
    """Exports all svgs within input_dir to pngs and stores them in the
    Android density-specific sub-directories within the output_dir.

    Args:
        inkscape_path (str): File path to the Inkscape program.
        input_dir (str): Path to the input directory containing svgs.
        output_dir (str): Path to the output directory; after this function
            returns, it will contain various density-specific sub-directories,
            which each contain the exported pngs.
        is_drawable (bool): If True, sub-directories are drawable directories
            (e.g. drawable-mdpi). Else, they are mipmap directories
            (e.g. mipmap-mdpi).
        width_dp (int): The width of the output png in the Android dp unit
            (not the Inkscape dpi unit).
        height_dp (int or None): Same as width_dp, but for height instead.
            If None, Inkscape determines it from the aspect ratio of the svg.
    """
    android_helper.make_density_dirs(output_dir, is_drawable)
    densities = android_helper.DENSITIES

    widths = android_helper.get_px_values_at_all_densities(width_dp)

    if height_dp is None:
        heights = [None for i in xrange(len(densities))]
    else:
        heights = android_helper.get_px_values_at_all_densities(height_dp)

    for i in xrange(len(densities)):
        density_specific_output_dir = android_helper.get_child_dir(
                output_dir, is_drawable, densities[i])
        export_svgs(inkscape_path, input_dir, density_specific_output_dir,
                    widths[i], heights[i])


def export_svgs(inkscape_path, input_dir, output_dir, width_px, height_px):
    for svg_path in get_svg_paths(input_dir):
        png_path = get_png_path(output_dir, get_svg_name(svg_path))
        export(inkscape_path, svg_path, png_path, width_px, height_px)


def get_svg_paths(dir_containing_svgs):
    svg_paths = []
    for file_ in os.listdir(dir_containing_svgs):
        if file_.endswith(".svg"):
            svg_paths.append(dir_containing_svgs + os.path.sep + file_)
    if len(svg_paths) == 0:
        print "No svgs found!"
    return svg_paths


def get_svg_name(svg_path):
    return (svg_path.split(os.path.sep)[-1]).split(".svg")[0]


def get_png_path(output_dir, png_name):
    return output_dir + os.path.sep + png_name + ".png"


def export(inkscape_path, svg_path, png_path, w, h):
    execute(build_command_list(inkscape_path, svg_path, png_path, w, h))


def execute(shell_command_as_list):
    shell_output = subprocess.check_output(shell_command_as_list)
    if verbose:
        print shell_output


def build_command_list(inkscape_path, svg_path, png_path, width, height):
    """Builds a list of shell commands necessary to convert a given Inkscape
    svg file to an output png file. If the height is not specified, Inkscape
    computes the height of the png file automatically from the aspect ratio.
    """
    # For more params, see https://inkscape.org/en/doc/inkscape-man.html
    shell_command_as_list = [
        inkscape_path,
        "--without-gui",
        "--export-area-page",
        "--export-png=%s" % (png_path),
        "--export-width=%d" % (width)]

    if height is not None:
        shell_command_as_list.append("--export-height=%d" % height)

    shell_command_as_list.append(svg_path)
    return shell_command_as_list


def get_default_inkscape_path():
    if os.name == "nt":
        windows_path1 = "C:\\Program Files\\Inkscape\\inkscape.exe"
        if os.path.isfile(windows_path1):
            return windows_path1
        windows_path2 = "C:\\Program Files (x86)\\Inkscape\\inkscape.exe"
        if os.path.isfile(windows_path2):
            return windows_path2
        return None
    else:
        mac_path = ("/Applications/Inkscape.app" +
                    "/Contents/Resources/bin/inkscape-bin")
        if os.path.isfile(mac_path):
            return mac_path
        linux_path = "/usr/bin/inkscape"
        if os.path.isfile(linux_path):
            return linux_path
        return None


def str_to_bool(input_str):
    return input_str.upper() in ("YES", "Y", "TRUE", "T", "1")


if __name__ == "__main__":
    default_inkscape_path = get_default_inkscape_path()

    default_input_dir = os.getcwd()
    default_output_dir = os.getcwd()
    default_is_drawable = "True"
    default_is_android = "False"
    default_height = None

    if verbose:
        default_is_verbose = "True"
    else:
        default_is_verbose = "False"

    parser = argparse.ArgumentParser()

    if default_inkscape_path is None:
        parser.add_argument("inkscape_path",
                            help="path to your Inkscape program")
    else:
        parser.add_argument("-inkscape", dest="inkscape_path",
                            help="path to your Inkscape program, " +
                            "defaults to %s" % (default_inkscape_path),
                            default=default_inkscape_path)

    parser.add_argument("-i", dest="input_dir",
                        help="path to the dir containing your svg(s), " +
                        "defaults to %s" % default_input_dir,
                        default=default_input_dir)

    parser.add_argument("-o", dest="output_dir",
                        help="path to the dir that will contain the output, " +
                        "defaults to %s" % default_output_dir,
                        default=default_output_dir)

    parser.add_argument("width", type=int,
                        help="width of the exported pngs (in Android dp " +
                        "if IS_ANDROID is True, in px otherwise)")

    parser.add_argument("-height", dest="height", type=int,
                        help="height of the exported pngs (in Android dp " +
                        "if IS_ANDROID is True, in px otherwise), defaults " +
                        "to None which lets Inkscape automatically compute " +
                        "the height based on the aspect ratio of the svg",
                        default=default_height)

    parser.add_argument("-a", dest="is_android",
                        help="specify whether the script should create " +
                        "different outputs for each Android display " +
                        "density, defaults to %s" % default_is_android,
                        default=default_is_android)

    parser.add_argument("-d", dest="is_drawable",
                        help="specify whether the output directories are " +
                        "for Android drawable or mipmap images, " +
                        "defaults to %s" % default_is_drawable +
                        "; ignore this if IS_ANDROID is False",
                        default=default_is_drawable)

    parser.add_argument("-v", dest="is_verbose",
                        help="enable to view shell output, " +
                        "defaults to %s" % default_is_verbose,
                        default=default_is_verbose)

    ###

    args = parser.parse_args()

    print "\n" + str(args) + "\n"

    verbose = str_to_bool(args.is_verbose)

    if str_to_bool(args.is_android):
        export_svgs_android_densities(args.inkscape_path,
                                      args.input_dir, args.output_dir,
                                      str_to_bool(args.is_drawable),
                                      args.width, args.height)
    else:
        export_svgs(args.inkscape_path,
                    args.input_dir, args.output_dir,
                    args.width, args.height)
