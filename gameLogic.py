from OpenGL.GL import *
from player import Player
from cube import Cube


def generateTerrain(n) -> list[Cube]:
    cubeList = []
    for i in range(n):
        for j in range(n):
            c = Cube(i * 2, j * 2, 0, 1)
            cubeList += [c]
    return cubeList
