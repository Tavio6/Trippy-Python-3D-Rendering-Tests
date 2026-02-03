from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

angle = 0

def draw():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0,0,5, 0,0,0, 0,1,0)
    glRotatef(angle, 1, 1, 0)

    glBegin(GL_QUADS)

    glColor3f(1,0,0)
    glVertex3f(-1,-1,1); glVertex3f(1,-1,1); glVertex3f(1,1,1); glVertex3f(-1,1,1)

    glColor3f(0,1,0)
    glVertex3f(-1,-1,-1); glVertex3f(-1,1,-1); glVertex3f(1,1,-1); glVertex3f(1,-1,-1)

    glColor3f(0,0,1)
    glVertex3f(-1,-1,-1); glVertex3f(-1,-1,1); glVertex3f(-1,1,1); glVertex3f(-1,1,-1)

    glColor3f(1,1,0)
    glVertex3f(1,-1,-1); glVertex3f(1,1,-1); glVertex3f(1,1,1); glVertex3f(1,-1,1)

    glColor3f(0,1,1)
    glVertex3f(-1,1,-1); glVertex3f(-1,1,1); glVertex3f(1,1,1); glVertex3f(1,1,-1)

    glColor3f(1,0,1)
    glVertex3f(-1,-1,-1); glVertex3f(1,-1,-1); glVertex3f(1,-1,1); glVertex3f(-1,-1,1)

    glEnd()
    glutSwapBuffers()
    angle = (angle + 1) % 360

def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0,0,0,1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 640/480, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

def timer(value):
    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(640, 480)
glutCreateWindow(b"Rotating Cube")
init()
glutDisplayFunc(draw)
glutTimerFunc(0, timer, 0)
glutMainLoop()