import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = [
    [-1.0,-1.0,-1.0],
    [1.0,-1.0,-1.0],
    [1.0,1.0,-1.0],
    [-1.0,1.0,-1.0],
    [-1.0,-1.0,1.0],
    [1.0,-1.0,1.0],
    [1.0,1.0,1.0],
    [-1.0,1.0,1.0]
]
faces = (
    (0, 1, 2, 3),
    (3, 2, 6, 7),
    (7, 6, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 6, 2),
    (4, 0, 3, 7)
)
colors = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1),
    (0, 0, 0),
    (1, 1, 1)
)
def draw_cube():
    glBegin(GL_QUADS)
    for face in faces:
        for vertex in face:
            glColor3fv(colors[vertex])
            glVertex3fv(vertices[vertex])
    glEnd()
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)    
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube()
        pygame.display.flip()
        pygame.time.wait(10)
if __name__ == "__main__":
    main()
