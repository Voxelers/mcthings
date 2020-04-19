# McThings [![Documentation Status](https://readthedocs.org/projects/mcthings/badge/?version=latest)](https://mcthings.readthedocs.io/en/latest/?badge=latest)

A framework for building a Creation with Things implemented using the
[Raspberry PI Minecraft](https://www.minecraft.net/en-us/edition/pi/)
[API](https://www.stuffaboutcode.com/p/minecraft-api-reference.html). It is based
on [mcpi library](https://github.com/martinohanlon/mcpi).

A Thing is a built based on blocks: [Pyramid](mcthings/pyramid.py), [River](mcthings/river.py),
[House](mcthings/house.py), [Fence](mcthings/fence.py)
and may others. All the Things share the [Thing API](mcthings/thing.py).

A [Creation is a list](mcthings/creation.py) of Things built in a specific position. Creations can be shared
loading and saving them to a [files](tests/creation.mct). All the [tests](tests) are creations. [This one](tests/creation.py) includes
a river, a house in each side of the river and a bridge for crossing the river.

![A Creation in Minecraft](creation.png)