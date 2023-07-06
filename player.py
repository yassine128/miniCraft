import pygame
from OpenGL.GL import *


class Player:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.COLLISION_THRESHOLD = 0.1
        self.rotation_angleX = 0
        self.up_down_angle = 0

    def collision(self, cube) -> bool:
        # Get the coordinates of the cube's bounding box
        cube_min_x = min(vertex[0] for vertex in cube.vertices)
        cube_max_x = max(vertex[0] for vertex in cube.vertices)
        cube_min_y = min(vertex[1] for vertex in cube.vertices)
        cube_max_y = max(vertex[1] for vertex in cube.vertices)
        cube_min_z = min(vertex[2] for vertex in cube.vertices)
        cube_max_z = max(vertex[2] for vertex in cube.vertices)

        # Check for overlap on all three axes
        if cube_min_x <= self.x <= cube_max_x and cube_min_y <= self.y <= cube_max_y and cube_min_z <= self.z <= cube_max_z:
            return True
        return False

    def move(self, keypress, listCube) -> None:
        # Store the current position for collision checking
        prev_x, prev_y, prev_z = self.x, self.y, self.z
        movement = {
            pygame.K_a: (0.1, 0, 0),
            pygame.K_d: (-0.1, 0, 0),
            pygame.K_w: (0, 0, 0.1),
            pygame.K_s: (0, 0, -0.1),
            pygame.K_SPACE: (0, -0.1, 0),
            pygame.K_x: (0, 0.1, 0),
        }
        for key, (dx, dy, dz) in movement.items():
            if keypress[key]:
                self.x += dx
                self.z += dz
                self.y += dy
        glTranslatef(self.x - prev_x, self.y - prev_y, self.z - prev_z)

    def getPosition(self):
        return self.x, self.y, self.z
