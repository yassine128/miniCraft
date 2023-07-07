from OpenGL.GL import *

class Cube:
    def __init__(self, x, y, z, size) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.size = size
        self.colors = (
            (0.4, 0.2, 0),
            (0.4, 0.2, 0),
            (0, 1, 0),
            (0.4, 0.2, 0),
            (0.4, 0.2, 0),
            (0.4, 0.2, 0),
            (0.4, 0.2, 0),
            (0.4, 0.2, 0),
            (0.4, 0.2, 0),
            (0.4, 0.2, 0),
            (0.4, 0.2, 0),
            (0.4, 0.2, 0)
        )

        self.surfaces = (
            (0,1,2,3),
            (3,2,7,6),
            (6,7,5,4),
            (4,5,1,0),
            (1,5,7,2),
            (4,0,3,6)
            )

        self.vertices = (
            (x + size, y - size, z - size),
            (x + size, y + size, z - size),
            (x - size, y + size, z - size),
            (x - size, y - size, z - size),
            (x + size, y - size, z + size),
            (x + size, y + size, z + size),
            (x - size, y - size, z + size),
            (x - size, y + size, z + size)
            )

        self.edges = (
            (0,1),
            (0,3),
            (0,4),
            (2,1),
            (2,3),
            (2,7),
            (6,3),
            (6,4),
            (6,7),
            (5,1),
            (5,4),
            (5,7)
            )

    def draw(self):
        glBegin(GL_QUADS)
        for i, surface in enumerate(self.surfaces):
            glColor3fv(self.colors[i])  # Assign color directly to each face
            for vertex in surface:
                glVertex3fv(self.vertices[vertex])
        glEnd()

        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3f(*self.vertices[vertex])
        glEnd()


class woodCube(Cube):
    def __init__(self, x, y, z, size):
        super().__init__(x, y, z, size)
        self.colors = (
            (1, 0.6, 0.2),
            (1, 0.6, 0.2),
            (1, 0.6, 0.2),
            (1, 0.6, 0.2),
            (1, 0.6, 0.2),
            (1, 0.6, 0.2),
        )

