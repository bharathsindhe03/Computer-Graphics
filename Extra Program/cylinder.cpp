#include <GL/glut.h>
#include <cmath>

void init() {
    gluOrtho2D(0, 400, 0, 400);
}

void display() {
    glClearColor(1, 1, 1, 1);
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(1, 0, 0);
    glPointSize(5);

    glBegin(GL_POINTS);
    for (int i = 0; i < 50; i++) {
        for (int j = 0; j < 36; j++) {
            double angle = j * 3.14159265 / 18;
            glVertex2f(200 + 50 * cos(angle), i * 7 + 50 * sin(angle));
        }
    }
    glEnd();
    glFlush();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(500, 500);
    glutInitWindowPosition(100, 100);
    glutCreateWindow("Cylinder");
    init();
    glutDisplayFunc(display);
    glutMainLoop();

    return 0;
}
