#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo


import argparse
import logging
import sys

from mcpi.vec3 import Vec3

from mcthings.vox import Vox


def parse_args():
    """Parse command line arguments"""

    parser = argparse.ArgumentParser()

    parser.add_argument('voxfile')
    parser.add_argument('-o', '--outfile', help='Schematic filename', required=False)

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    return parser.parse_args()


def load_vox_file(vox_file):
    # The position should be optional. If not, we have a desing issue for this use case
    voxels = Vox(Vec3(0, 0, 0 ))
    voxels.file_path = vox_file
    # load the voxels in memory
    voxels.create()

    return voxels


def main():
    logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] - %(message)s")

    args = parse_args()

    vox_file = sys.argv[1]
    schematic_file = vox_file.replace(".vox", ".schematic")

    if args.outfile:
        schematic_file = args.outfile

    logging.info("Vox input file: %s", vox_file)
    logging.info("Schematic output file: %s", schematic_file)

    voxels = load_vox_file(vox_file)
    # TODO: Reimplement Thing to schematic to worl always from memory?
    voxels._blocks_memory.to_schematic(schematic_file)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        s = "\n\nReceived Ctrl-C or other break signal. Exiting.\n"
        sys.stderr.write(s)
        sys.exit(0)