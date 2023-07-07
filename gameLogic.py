from OpenGL.GL import *
from OpenGL.raw.GLU import *

from player import Player
from cube import Cube, woodCube
import numpy as np


def generateTerrain(n) -> list[Cube]:
    cubeList = []
    for i in range(n):
        for j in range(n):
            c = Cube(i * 2, j * 2, 0, 1)
            cubeList += [c]
    return cubeList


def addCube(cubeList, cube):
    if cube is not None:
        cubeList.append(woodCube(cube.x, cube.y, cube.z + 2, 1))


def delCube(cubeList, cube):
    if cube is not None:
        cubeList.remove(cube)


def pick_object(x, y, cubeList):
    viewport = glGetIntegerv(GL_VIEWPORT)
    depth = glReadPixels(x, viewport[3] - y, 1, 1, GL_DEPTH_COMPONENT, GL_FLOAT)

    modelview_matrix = glGetDoublev(GL_MODELVIEW_MATRIX)
    projection_matrix = glGetDoublev(GL_PROJECTION_MATRIX)
    window_x = x
    window_y = viewport[3] - y

    world_x = (GLdouble * 1)(0.0)
    world_y = (GLdouble * 1)(0.0)
    world_z = (GLdouble * 1)(0.0)

    gluUnProject(window_x, window_y, depth, modelview_matrix, projection_matrix, viewport, world_x, world_y, world_z)

    world_x = world_x[0]
    world_y = world_y[0]
    world_z = world_z[0]

    selected_object = None
    for cube in cubeList:
        if (int(world_x), int(world_y), int(world_z)) == (cube.x, cube.y, cube.z):
            selected_object = cube
            break

    return selected_object
