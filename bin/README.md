vox2schematic
--

A conversion tool that reads a vox file with one model 
in original or current format and converts it voxel by voxel 
to blocks in a Minecraft Schematic file. 
The voxels are converted to wool blocks, and the color of the voxels 
are mapped to one of the 16 possible wools colors in the blocks.

There is a [MagicaVoxel palette](https://github.com/Voxelers/mcthings/blob/develop/tests/integration/vox/minecraft_wool_palette.png) 
with the wool colors. If you use it in your model, the colors in Schematic blocks will be the same than the voxels ones.

To install it just execute:

`pip install mcthings`

To execute it:

`vox2schematic model.vox`

and a `model.schematic` file will be created in the same directory.

[Design and implementation details](https://github.com/Voxelers/mcthings/issues/99)
