from mcpi.minecraft import Minecraft
import minecraft_material as mm
import math

mc = Minecraft.create()

class Cuboid:
    def __init__(self, x, y, z, length, width, height, material):
        self.x = x
        self.y = y
        self.z = z
        self.length = length
        self.width = width
        self.height = height
        self.material = material

    @staticmethod
    def parseFromLine(line):
        params = [w for w in line.strip().split(',')]
        if len(params) < 7:
            return None
        for i in range(len(params)-1):
            params[i] = float(params[i])
        return Cuboid(params[0], params[1], params[2], params[3], params[4], params[5], params[6])

    def create_matrix(self):
        res = []
        for x in range(round(self.width)):
            for y in range(round(self.length)):
                for z in range(round(self.height)):
                    res.append((x, z, y))
        return res

    def build(self, x, z, y):
        if self.length <= 0 or self.width <= 0 or self.height <= 0:
            return
        x += self.x
        y += self.y
        z += self.z
        mc.setBlocks(x, z, y,
                     x + self.length-1, z + self.height-1, y + self.width-1,
                     mm.Material[self.material])
        # mc.setBlocks(x + 1, z + 1, y + 1,
        #              x + self.width - 1, z + self.height - 1, y + self.length - 1,
        #              mm.Material["AIR"])


class TrianglePrismX:
    def __init__(self, x, y, z, length, width, material):
        self.x = x
        self.y = y
        self.z = z
        self.length = length
        self.width = width
        self.material = material

    @staticmethod
    def parseFromLine(line):
        params = [w for w in line.strip().split(',')]
        if len(params) < 6:
            return None
        for i in range(len(params) - 1):
            params[i] = float(params[i])
        return TrianglePrismX(params[0], params[1], params[2], params[3], params[4], params[5])

    def create_matrix(self):
        res = []
        length = self.length
        shift = 0
        z = 0
        while length >= 0:
            for y in range(round(self.width)):
                for x in range(length):
                    res.append((x+shift, z, y))
            length -= 2
            shift += 1
        return res

    def build(self, x, z, y):
        if self.length <= 0 or self.width <= 0: return
        x += self.x
        y += self.y
        z += self.z
        length = self.length-1
        shift = 0
        while length >= 0:
            mc.setBlocks(x + shift, z + shift, y, x + shift + length, z + shift, y + self.width-1, mm.Material[self.material])
            length -= 2
            shift += 1
        # length = self.length-5
        # shift = 2
        # z_shift = 1
        # while length > 0:
        #     mc.setBlocks(x + shift, z + z_shift, y + 1, x + shift + length, z + z_shift, y + self.width - 2,
        #                  mm.Material["AIR"])
        #     length -= 2
        #     shift += 1

class TrianglePrismY:
    def __init__(self, x, y, z, length, width, material):
        self.x = x
        self.y = y
        self.z = z
        self.length = length
        self.width = width
        self.material = material

    @staticmethod
    def parseFromLine(line):
        params = [w for w in line.strip().split(',')]
        if len(params) < 6:
            return None
        for i in range(len(params) - 1):
            params[i] = float(params[i])
        return TrianglePrismY(params[0], params[1], params[2], params[3], params[4], params[5])

    def build(self, x, z, y):
        if self.length <= 0 or self.width <= 0: return
        x += self.x
        y += self.y
        z += self.z
        length = self.length-1
        shift = 0
        while length >= 0:
            mc.setBlocks(x + shift, z + shift, y, x + shift + self.width-1, z + shift, y + length, mm.Material[self.material])
            length -= 2
            shift += 1

class Sphere:
    def __init__(self, x, y, z, r, material):
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.material = material

    @staticmethod
    def parseFromLine(line):
        params = [w for w in line.strip().split(',')]
        if len(params) < 5:
            return None
        return Sphere(float(params[0]), float(params[1]), float(params[2]), float(params[3]), params[4])

    def create_matrix(self):
        res = []
        for iz in range(round(self.r)):
            rho = self.r * math.sqrt(1 - iz / self.r)
            for ix in range(round(rho)):
                ry = rho * math.sqrt(1 - ix / rho)
                for iy in range(round(ry)):
                    res.append((x + ix, z + iz, y + iy))
                    res.append((x - ix, z + iz, y + iy))
                    res.append((x + ix, z + iz, y - iy))
                    res.append((x - ix, z + iz, y - iy))
                    res.append((x + ix, z - iz, y + iy))
                    res.append((x - ix, z - iz, y + iy))
                    res.append((x + ix, z - iz, y - iy))
                    res.append((x - ix, z - iz, y - iy))
        return res

    def build(self, x, z, y):
        x += self.x + self.r - 1
        y += self.y + self.r - 1
        z += self.z + self.r - 1

        for iz in range(round(self.r)):
            rho = self.r * math.sqrt(1 - iz / self.r)
            for ix in range(round(rho)):
                ry = rho * math.sqrt(1 - ix / rho)
                for iy in range(round(ry)):
                    mc.setBlock(x + ix, z + iz, y + iy, mm.Material[self.material])
                    mc.setBlock(x - ix, z + iz, y + iy, mm.Material[self.material])
                    mc.setBlock(x + ix, z + iz, y - iy, mm.Material[self.material])
                    mc.setBlock(x - ix, z + iz, y - iy, mm.Material[self.material])
                    mc.setBlock(x + ix, z - iz, y + iy, mm.Material[self.material])
                    mc.setBlock(x - ix, z - iz, y + iy, mm.Material[self.material])
                    mc.setBlock(x + ix, z - iz, y - iy, mm.Material[self.material])
                    mc.setBlock(x - ix, z - iz, y - iy, mm.Material[self.material])

class CylinderZ:
    def __init__(self, x, y, z, r, h, material):
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.h = h
        self.material = material

    @staticmethod
    def parseFromLine(line):
        params = [w for w in line.strip().split(',')]
        if len(params) < 5:
            return None
        return CylinderZ(
            float(params[0]), float(params[1]), float(params[2]),
            float(params[3]), float(params[4]),
            params[5]
        )

    def create_matrix(self):
        res = []
        for z in range(round(self.h)):
            for x in range(self.r):
                ry = self.r * math.sqrt(1 - x / self.r)
                for y in range(round(ry)):
                    res.append((x, z, y))
                    if x != 0:
                        res.append((-x, z, y))
                    if y != 0:
                        res.append((x, z, -y))
                        if x != 0:
                            res.append((-x, z, -y))
        return res

    def build(self, x, z, y):
        x += self.x + self.r - 1
        y += self.y + self.r - 1
        z += self.z

        for iz in range(round(self.h)):
            for ix in range(round(self.r)):
                ry = self.r * math.sqrt(1 - ix / self.r)
                for iy in range(round(ry)):
                    mc.setBlock(x + ix, z + iz, y + iy, mm.Material[self.material])
                    if ix != 0:
                        mc.setBlock(x - ix, z + iz, y + iy, mm.Material[self.material])
                    if iy != 0:
                        mc.setBlock(x + ix, z + iz, y - iy, mm.Material[self.material])
                        if ix != 0:
                            mc.setBlock(x - ix, z + iz, y - iy, mm.Material[self.material])


class MinecraftBlock:
    def __init__(self, x, y, z, type):
        self.x = x
        self.y = y
        self.z = z
        self.type = type

    @staticmethod
    def parseFromLine(line):
        params = [w for w in line.strip().split(',')]
        if len(params) < 4:
            return None
        for i in range(len(params) - 1):
            params[i] = float(params[i])
        return MinecraftBlock(params[0], params[1], params[2], params[3])

    def build(self, x, z, y):
        x += self.x
        y += self.y
        z += self.z
        mc.setBlock(x, z, y, mm.Material["AIR"])
        mc.setBlock(x, z, y, mm.Material[self.type])

def parseLine(line):
    words = line.split(':')
    if len(words) < 2:
        return None
    if words[0] == 'P':
        return Cuboid.parseFromLine(words[1])
    elif words[0] == 'TPX':
        return TrianglePrismX.parseFromLine(words[1])
    elif words[0] == 'TPY':
        return TrianglePrismY.parseFromLine(words[1])
    elif words[0] == 'S':
        return Sphere.parseFromLine(words[1])
    elif words[0] == 'CZ':
        return CylinderZ.parseFromLine(words[1])
    elif words[0] == 'OBJ':
        return MinecraftBlock.parseFromLine(words[1])
    mc.postToChat("Unknown object " + words[0])
    return None


def script_file_reader(filename):
    objs = []
    with open(filename, 'r') as f:
        for line in f:
            objs.append(parseLine(line))
    return objs


if __name__ == "__main__":
    objs = script_file_reader("script.sc")
    while True:
        hits = mc.events.pollBlockHits()
        if hits:
            x, z, y = hits[0].pos.x, hits[0].pos.y, hits[0].pos.z
            mc.postToChat(f"pos: {x},{z},{y}")
            for o in objs:
                if o:
                    o.build(x, z, y)
            break
