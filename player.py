import pygame 
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import math
 

class Player: 
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x 
        self.y = y
        self.z = z
        self.COLLISION_THRESHOLD = 0.1

    def collision(self, cube):
        # Get the coordinates of the cube's bounding box
        cube_min_x = min(vertex[0] for vertex in cube.vertices)
        cube_max_x = max(vertex[0] for vertex in cube.vertices)
        cube_min_y = min(vertex[1] for vertex in cube.vertices)
        cube_max_y = max(vertex[1] for vertex in cube.vertices)
        cube_min_z = min(vertex[2] for vertex in cube.vertices)
        cube_max_z = max(vertex[2] for vertex in cube.vertices)
        #print(cube_min_x, cube_max_x, cube_min_z, cube_max_z, self.x, self.z)

        # Check for overlap on all three axes
        if cube_min_x <= self.x <= cube_max_x and cube_min_y <= self.y <= cube_max_y and cube_min_z <= self.z <= cube_max_z:
            return True 
        return False

    def move(self, event, cube):
        if event.type == pygame.KEYDOWN:
            # Store the current position for collision checking
            prev_x, prev_y, prev_z = self.x, self.y, self.z
            movement = {
                pygame.K_LEFT: (0.1, 0),
                pygame.K_RIGHT: (-0.1, 0),
                pygame.K_UP: (0, 0.1),
                pygame.K_DOWN: (0, -0.1)
            }

            for key, (dx, dz) in movement.items():
                if event.key == key:
                    self.x += dx
                    self.z += dz
                    if self.collision(cube):
                        self.x -= dx
                        self.z -= dz

            glTranslatef(self.x - prev_x, 0, self.z - prev_z)

    def getPosition(self):
        return (self.x, self.y, self.z)