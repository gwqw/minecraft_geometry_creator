# Minecraft geometry creator

Simple script language for drawing (creating) Minecraft 3D primitives



## 3D objects

X:x,y,z,params,material

X - object type

- P - cuboid, params: length, width, height
- S - sphere, params: radius, height
- CZ - cylinder z-coaxial
- TPX, TPY - triangle prizm x,y-coaxial
- OBJ - minecraft block



## Material

AIR, STONE, GRASS, DIRT, COBBLE, WOOD_PLANKS, SAND, WOOD, GLASS, BED, WOOL, GOLDEN_BLOCK, IRON_BLOCK, BRICK, TORCH, OAK_STAIRS, CHEST, WOODEN_DOOR



## Example "script.sc"

P:0,0,5,5,4,3,WOOL -- cuboid in (0,0,5) with L:W:H = 5:4:3 with material WOOL