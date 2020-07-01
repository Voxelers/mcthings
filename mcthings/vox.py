# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author/s (©): Alvaro del Castillo

import chunk

import mcpi.block
from mcpi.vec3 import Vec3

from mcthings.thing import Thing


class Voxel:
    def __init__(self, bytes):
        self.x = bytes[0]
        self.y = bytes[1]
        self.z = bytes[2]
        self.color_index = bytes[3] - 1


class Color:
    """ RGBA format palette """
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def to_hex_str(self):
        # rgb
        hex_str = self.r.hex() + self.g.hex() + self.b.hex()

        return hex_str

    def minecraft(self):
        # https://gaming.stackexchange.com/questions/47212/what-are-the-color-values-for-dyed-wool
        mc_colors = [
            ("White", "e4e4e4"),
            ("Orange", "ea7e35"),
            ("Magenta", "be49c9"),
            ("Light Blue", "6387d2"),
            ("Yellow", "c2b51c"),
            ("Lime", "39ba2e"),
            ("Pink", "d98199"),
            ("Grey", "414141"),
            ("Light grey", "a0a7a7"),
            ("Cyan", "267191"),
            ("Purple", "7e34bf"),
            ("Blue", "253193"),
            ("Brown", "56331c"),
            ("Green", "364b18"),
            ("Red", "9e2b27"),
            ("Black", "181414")
        ]

        mc_color_number = {}
        mc_color_hex = {}
        for i in range(0, len(mc_colors)):
            mc_color_number[mc_colors[i][0]] = i
            mc_color_hex[mc_colors[i][1]] = mc_colors[i][0]

        # Simple mapping: R, G or B
        if self.r > self.g and self.r > self.b:
            color = "Red"
        elif self.g > self.r and self.g > self.b:
            color = "Green"
        elif self.b > self.r and self.b > self.g:
            color = "Blue"
        else:
            # All components are the same, let's select Red now
            color = "Red"

        # Direct mapping
        if self.to_hex_str() in mc_color_hex:
            color = mc_color_hex[self.to_hex_str()]

        return mc_color_number[color]


class Vox(Thing):
    file_path = None
    """ file path for the MagicaVoxel vox file """

    def __init__(self, pos):
        self.voxels = []
        self.palette = []

        super().__init__(pos)

    def is_legacy_vox(self):
        legacy = False
        if not self.file_path:
            RuntimeError("Missing file_path param")
        vox_file = open(self.file_path, "rb")
        vox_chunk = chunk.Chunk(vox_file, bigendian=False)
        chunk_name = vox_chunk.getname().decode("utf-8")
        version = vox_chunk.chunksize
        vox_file.close()

        if version != 150:
            legacy = True

        return legacy

    def parse_vox_file_legacy(self):
        """
        VOX
        MAIN
        SIZE
        XYZI
        RGBA (empty if it is the default one)
        :return:
        """
        vox_file = open(self.file_path, "rb")
        vox_chunk = chunk.Chunk(vox_file, bigendian=False)
        main_chunk = chunk.Chunk(vox_file, bigendian=False)
        vox_file.seek(vox_file.tell() + 4)
        size_chunk = chunk.Chunk(vox_file, bigendian=False)
        vox_file.seek(vox_file.tell() + 4)  # number of children chunks
        x = size_chunk.read(4)
        y = size_chunk.read(4)
        z = size_chunk.read(4)
        xyzi_chunk = chunk.Chunk(vox_file, bigendian=False)
        vox_file.seek(vox_file.tell() + 4)  # number of children chunks
        n_voxels_bytes = xyzi_chunk.read(4)
        n_voxels = int.from_bytes(n_voxels_bytes, "little")
        for i in range(0, n_voxels):
            self.voxels.append(Voxel(xyzi_chunk.read(4)))
        rgba_chunk = chunk.Chunk(vox_file, bigendian=False)
        vox_file.seek(vox_file.tell() + 4)  # number of children chunks
        for i in range(0, round(rgba_chunk.getsize()/4)):
            self.palette.append(Color(rgba_chunk.read(1),
                                      rgba_chunk.read(1),
                                      rgba_chunk.read(1),
                                      rgba_chunk.read(1)))

    def parse_vox_file(self):
        if not self.file_path:
            RuntimeError("Missing file_path param")

        # Read the vox data in RIFF format
        # https://github.com/python/cpython/blob/3.8/Lib/chunk.py
        vox_file = open(self.file_path, "rb")
        vox_chunk = chunk.Chunk(vox_file, bigendian=False)
        chunk_name = vox_chunk.getname().decode("utf-8")
        version = vox_chunk.chunksize
        if version != 150:
            raise RuntimeError('File %s has a not supported VOX version %i' % (self.file_path, version))
        if chunk_name != 'VOX ':
            raise RuntimeError('File %s is not a VOX file' % self.file_path)
        # Let's read chunks
        """
        2. Chunk Structure
        -------------------------------------------------------------------------------
        # Bytes  | Type       | Value
        -------------------------------------------------------------------------------
        1x4      | char       | chunk id
        4        | int        | num bytes of chunk content (N)
        4        | int        | num bytes of children chunks (M)      
        N        |            | chunk content
        M        |            | children chunks
        -------------------------------------------------------------------------------
        """
        # MAIN Chunk
        main_chunk = chunk.Chunk(vox_file, bigendian=False)
        # Pass last 4 bytes for MAIN Chunk with children chunks
        vox_file.seek(vox_file.tell() + 4)

        # SIZE CHUNK
        """
        -------------------------------------------------------------------------------
        # Bytes  | Type       | Value
        -------------------------------------------------------------------------------
        4        | int        | size x
        4        | int        | size y
        4        | int        | size z : gravity direction
        -------------------------------------------------------------------------------
        """
        size_chunk = chunk.Chunk(vox_file, bigendian=False)
        vox_file.seek(vox_file.tell() + 4)  # number of children chunks
        x = size_chunk.read(4)
        y = size_chunk.read(4)
        z = size_chunk.read(4)
        # vox_file.seek(vox_file.tell() + 4)  # children chunks
        # XYZI voxels
        """
        -------------------------------------------------------------------------------
        # Bytes  | Type       | Value
        -------------------------------------------------------------------------------
        4        | int        | numVoxels (N)
        4 x N    | int        | (x, y, z, colorIndex) : 1 byte for each component
        -------------------------------------------------------------------------------
        """
        xyzi_chunk = chunk.Chunk(vox_file, bigendian=False)
        vox_file.seek(vox_file.tell() + 4)  # number of children chunks
        n_voxels_bytes = xyzi_chunk.read(4)
        n_voxels = int.from_bytes(n_voxels_bytes, "little")
        for i in range(0, n_voxels):
            self.voxels.append(Voxel(xyzi_chunk.read(4)))
        # Transform or palette chunk
        transform_chunk = chunk.Chunk(vox_file, bigendian=False)
        if transform_chunk.chunkname.decode("utf-8") == "nTRN":
            vox_file.seek(vox_file.tell() + 4)  # number of children chunks
            transform_chunk.skip()

            group_chunk = chunk.Chunk(vox_file, bigendian=False)
            vox_file.seek(vox_file.tell() + 4)  # number of children chunks
            group_chunk.skip()

            transform_chunk = chunk.Chunk(vox_file, bigendian=False)
            vox_file.seek(vox_file.tell() + 4)  # number of children chunks
            # transform_chunk.skip()  # it is skipping 1 byte in the next chunk
            vox_file.read(transform_chunk.getsize())

            shape_chunk = chunk.Chunk(vox_file, bigendian=False)
            vox_file.seek(vox_file.tell() + 4)  # number of children chunks
            vox_file.read(shape_chunk.getsize())

            # Layers chunk
            NUM_LAYERS = 8  # By default
            for i in range(0, NUM_LAYERS):
                layer_chunk = chunk.Chunk(vox_file, bigendian=False)
                vox_file.seek(vox_file.tell() + 4)  # number of children chunks
                vox_file.read(layer_chunk.getsize())
            """
            7. Chunk id 'RGBA' : palette
            -------------------------------------------------------------------------------
            # Bytes  | Type       | Value
            -------------------------------------------------------------------------------
            4 x 256  | int        | (R, G, B, A) : 1 byte for each component
                                  | * <NOTICE>
                                  | * color [0-254] are mapped to palette index [1-255], e.g : 
                                  | 
                                  | for ( int i = 0; i <= 254; i++ ) {
                                  |     palette[i + 1] = ReadRGBA(); 
                                  | }
            -------------------------------------------------------------------------------
            """
            rgba_chunk = chunk.Chunk(vox_file, bigendian=False)
            vox_file.seek(vox_file.tell() + 4)  # number of children chunks
        else:
            rgba_chunk = transform_chunk
        for i in range(0, round(rgba_chunk.getsize()/4)):
            self.palette.append(Color(rgba_chunk.read(1),
                                      rgba_chunk.read(1),
                                      rgba_chunk.read(1),
                                      rgba_chunk.read(1)))
        # Not need the rest of Chunks yet
        # matt_chunk = chunk.Chunk(vox_file, bigendian=False)

    def create(self):
        if not self.is_legacy_vox():
            self.parse_vox_file()
        else:
            self.parse_vox_file_legacy()

        for voxel in self.voxels:
            voxel_color = self.palette[voxel.color_index]
            minecraft_color = voxel_color.minecraft()

            # y, z are the reverse in vox format
            self.set_block(Vec3(self.position.x + voxel.x,
                                self.position.y + voxel.z,
                                self.position.z + voxel.y
                                ),
                                mcpi.block.WOOL.id, minecraft_color)

        init_pos, end_pos = self._blocks_memory.find_init_end_pos()
        self._end_position = end_pos
