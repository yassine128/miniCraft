import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from player import Player
from cube import Cube

import numpy as np 

"""
Quick version of minecraft 
Implementing : 
    - Player movement [X]
    - Collision [X]
    - Textures [X]
    - Cubes 
    - Maybe: Random cubes generation
"""

def get_camera_position():
    modelview_matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    camera_position = np.linalg.inv(modelview_matrix)[:3, 3]
    return tuple(camera_position)


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, display[0] / display[1], 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)
    camera_position = get_camera_position()

    player = Player(camera_position[0], camera_position[1], camera_position[2])
    cube = Cube()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print(get_camera_position())
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glClearColor(39/255, 149/255, 245/255, 0.8)
        player.move(event, cube)
        cube.draw()
        pygame.display.flip()
        pygame.time.wait(10)


main()