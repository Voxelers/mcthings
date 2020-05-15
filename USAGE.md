# McThings Usage

In order to use McThings you need Minecraft or Minetest running with Python support 
([Raspberry PI Minecraft](https://www.minecraft.net/en-us/edition/pi/)). Once you have
it you can start executing Python code using McThings to build the scenes in Minecraft/Minetest.

Jupyter Notebooks are great to start doing it, and the [scenes repository](scenes) uses this option.

But you can use also other Python environments like PyCharm.

[This is a research](https://github.com/juntosdesdecasa/mcthings/issues/50) of the current options to use Python in Minecraft and Minetest.

The options tested are:

## Minecraft Spigot server

This option works with the latest release of Minecraft at this moment: 1.15.2. Install in the Spigot server 
[this plugin](https://www.spigotmc.org/resources/raspberryjuice.22724/) and that's all.

## Minecraft Forge Client

In this case you don't need to run a server. Just start the Minecraft Forge client with 
[this plugin](https://github.com/arpruss/raspberryjammod) installed and in Single Player mode. 
Tested with the version **1.12.2**. The plugin does not work with newer versions. 
[Install process](https://github.com/juntosdesdecasa/mcthings/issues/38)

Probably the Forge server option will work also. 

## Minetest

For using Minetest, just install [this plugin](https://github.com/arpruss/raspberryjammod-minetest).
Minetest 5.1 has been tested but probably it will work with newer versions. [Install process](https://github.com/juntosdesdecasa/mcthings/issues/45)



