import struct

def color(r, g, b):
  return bytes([ int(b * 255), int(g* 255), int(r* 255)])

  
class Texture(object):
    def __init__(self, path):
        self.path = path
        self.read()

    def read(self):
        with open(self.path, "rb") as image:
            image.seek(10)
            headerSize = struct.unpack('=l', image.read(4))[0]

            image.seek(14 + 4)
            self.width = struct.unpack('=l', image.read(4))[0]
            self.height = struct.unpack('=l', image.read(4))[0]

            image.seek(headerSize)

            self.pixels = []

            for y in range(self.height):
                self.pixels.append([])
                for x in range(self.width):
                    b = ord(image.read(1)) / 255
                    g = ord(image.read(1)) / 255
                    r = ord(image.read(1)) / 255

                    self.pixels[y].append( color(r,g,b) )

    def getColor(self, tx, ty, intensity = 1):
        if 0<=tx<1 and 0<=ty<1:
            x = int(tx * self.width)
            y = int(ty * self.height)
            return self.pixels[y][x]
        else:
            return color(0,0,0)