#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

from mcpi.vec3 import Vec3

from mcthings.vox import Vox


class TestVox(unittest.TestCase):
    """Test Vox Thing"""

    def test_parse_vox_file(self):

        # Old format
        vox = Vox(Vec3(0, 0 ,0))
        vox.file_path = "vox/alien_engi1a.vox"
        vox.parse_vox_file()
        assert len(vox.voxels) == 180
        assert len(vox.palette) == 256

        # Old format with default palette
        vox1 = Vox(Vec3(0, 0 ,0))
        vox1.file_path = "vox/chr_beardo3-default-palette.vox"
        vox1.parse_vox_file()
        assert len(vox1.voxels) == 299
        assert len(vox1.palette) == 255  # 1 color less than before? bug?

        # New format
        vox2 = Vox(Vec3(0, 0 ,0))
        vox2.file_path = "vox/vxs.vox"
        vox2.parse_vox_file()
        assert len(vox2.voxels) == 3
        assert len(vox2.palette) == 256

    def test_voxel_position(self):
        vox2 = Vox(Vec3(0, 0 ,0))
        vox2.file_path = "vox/vxs.vox"
        vox2.parse_vox_file()

        # initial position of the voxelers logo
        #    *  *
        #     *
        # Base V block
        assert vox2.voxels[0].x == 1
        assert vox2.voxels[0].y == vox2.voxels[0].z == 0
        # Left V block
        assert vox2.voxels[1].x == vox2.voxels[1].y == 0
        assert vox2.voxels[1].z == 1
        # Right V block
        assert vox2.voxels[2].x == 2
        assert vox2.voxels[2].y == 0
        assert vox2.voxels[2].z == 1

    def test_voxel_color(self):
        vox2 = Vox(Vec3(0, 0 ,0))
        vox2.file_path = "vox/vxs.vox"
        vox2.parse_vox_file()

        # red color: ee0000ff
        color = vox2.palette[vox2.voxels[0].color_index]
        assert color.hex_str == 'ee0000ff'
        assert color.minecraft() == 14  # red


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
