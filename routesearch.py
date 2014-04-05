import os, sys
from PIL import Image, ImageChops, ImageMath

SPRITE_SIZE = 16

class Patch:
    def __init__(self, x1, x2, y):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y
        self.y2 = y + SPRITE_SIZE
    def add_grass(self):
        self.x2 += SPRITE_SIZE

class Route(Image.Image):
    def __init__(self, route_path, grass_path):
        self.route = Image.open(route_path)
        self.width, self.height = self.route.size

        self.grass = Image.open(grass_path)
        
        self.xstart, self.ystart = self.find_grass_start()
        self.xoffset = self.xstart % SPRITE_SIZE

    def find_grass_start(self):
        for y1 in range(0, self.height - SPRITE_SIZE + 1):
            y2 = y1 + SPRITE_SIZE
            for x1 in range(0, self.width - SPRITE_SIZE + 1):
                x2 = x1 + SPRITE_SIZE

                square = self.route.crop((x1, y1, x2, y2))
                diff = ImageChops.difference(square, self.grass)
                if sum(ImageMath.eval('int(diff)', diff=diff).histogram()) == 0:
                    return x1, y1

    def find_grass_patches(self):
        self.grass_patches = []
        x1, y1 = self.xstart, self.ystart

        while y1 <= self.height - SPRITE_SIZE:
            y2 = y1 + SPRITE_SIZE
            x1 = self.xoffset
            while x1 <= self.width - SPRITE_SIZE:
                x2 = x1 + SPRITE_SIZE

                square = self.route.crop((x1, y1, x2, y2))
                diff = ImageChops.difference(square, self.grass)

                if sum(ImageMath.eval('int(diff)', diff=diff).histogram()) == 0:
                    if self.grass_patches and\
                        self.grass_patches[-1].y1 == y1 and\
                        self.grass_patches[-1].x2 == x1:
                        self.grass_patches[-1].add_grass()
                    else:
                        self.grass_patches.append(Patch(x1, x2, y1))
                x1 += SPRITE_SIZE
            y1 += SPRITE_SIZE

        return self.grass_patches

def main(route_path, grass_path):
    route = Route(route_path, grass_path)

    return route.find_grass_patches()

if __name__ == '__main__':
    route_path = os.path.abspath(sys.argv[1])
    grass_path = os.path.abspath(sys.argv[2])

    patches = main(route_path, grass_path)
    total = 0
    for patch in patches:
        print(patch.x1, patch.y1, patch.x2, patch.y2)
        total += 1
    print('{} rows of grass'.format(total))

