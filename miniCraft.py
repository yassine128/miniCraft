import pygame
from pygame.locals import *

from OpenGL.GLU import *
from gameLogic import *

import numpy as np

"""
Simple version of minecraft 
Implementing : 
    - Player movement , Front Back [X], Mouse Rotation [X], Up-Down [X]
    - mouse orientation [X]
    - Textures [X]
    - Cubes [X]
    - Cube Adding [x]
    - Cube Removing [X]
"""


def get_camera_position():
    modelview_matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    camera_position = np.linalg.inv(modelview_matrix)[:3, 3]
    return tuple(camera_position)


def main():
    pygame.init()
    display = (800, 600)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])

    sphere = gluNewQuadric()

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    player = Player(0, 2, 0)
    gluLookAt(player.x, player.y, player.z, 0, 0, 0, 0, 0, 1)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    glLoadIdentity()

    # init mouse movement and center mouse on screen
    displayCenter = [screen.get_size()[i] // 2 for i in range(2)]
    mouseMove = [0, 0]
    pygame.mouse.set_pos(displayCenter)

    up_down_angle = 0.0
    paused = False
    run = True

    crosshair_color = (255, 255, 255)  # White color
    crosshair_size = 20
    crosshair_thickness = 2

    cubeList = generateTerrain(5)
    displayCenter = [screen.get_size()[i] // 2 for i in range(2)]

    # pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()

    screen_width = 800
    screen_height = 600

    while True:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(39 / 255, 149 / 255, 245 / 255, 0.8)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEMOTION:
                mouseMove = [event.pos[i] - displayCenter[i] for i in range(2)]  # Mouse movement
                pygame.mouse.set_pos(displayCenter)

        for c in cubeList:
            c.draw()

        keypress = pygame.key.get_pressed()
        cube = pick_object(screen_width // 2, screen_height // 2, cubeList)
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            addCube(cubeList, cube)
        if mouse[2]:
            delCube(cubeList, cube)

        glLoadIdentity()
        up_down_angle += mouseMove[1] * 0.3
        glRotatef(up_down_angle, 1.0, 0.0, 0.0)
        glPushMatrix()
        glLoadIdentity()
        player.move(keypress, cubeList)
        glRotatef(mouseMove[0] * 0.3, 0.0, 1.0, 0.0)
        glMultMatrixf(viewMatrix)
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
        glPopMatrix()
        glMultMatrixf(viewMatrix)

        clock.tick()

        pygame.display.flip()
        pygame.time.wait(5)


main()
