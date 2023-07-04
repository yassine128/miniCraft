from OpenGL.GL import *



class Cube: 
    def __init__(self) -> None:
        self.colors = (
            (1,0,0),
            (0,1,0),
            (0,0,1),
            (0,1,0),
            (1,1,1),
            (0,1,1),
            (1,0,0),
            (0,1,0),
            (0,0,1),
            (1,0,0),
            (1,1,1),
            (0,1,1),
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
            (1, -1, -1),
            (1, 1, -1),
            (-1, 1, -1),
            (-1, -1, -1),
            (1, -1, 1),
            (1, 1, 1),
            (-1, -1, 1),
            (-1, 1, 1)
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
        for surface in self.surfaces:
            x = 0
            for vertex in surface:
                x+=1
                glColor3fv(self.colors[x])
                glVertex3fv(self.vertices[vertex])
        glEnd()

        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()
