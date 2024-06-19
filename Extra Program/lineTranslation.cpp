#include <glut.h>
#include <cstdio>

float tx=50, ty=30;

void init() {
	glClearColor(1.0, 1.0, 1.0, 1.0);
	glColor3f(0.0, 0.0, 0.0);
	glPointSize(10.0);
	glLineWidth(2.0);
	glMatrixMode(GL_PROJECTION);
	gluOrtho2D(-200.0, 200.0, -200.0, 200.0);
}

void line(float x1,float y1, float x2, float y2) {
	glBegin(GL_LINES);
	glVertex2f(x1, y1);
	glVertex2f(x2, y2);
	glEnd();
}

void display() {
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(0.0, 0.0, 0.0); 
	line(-110.0, -110.0, 110.0, 110.0);
	glColor3f(1.0, 0.0, 0.0); 
	line(-110.0 + tx, -110.0 + ty, 110.0 + tx, 110.0 + ty);
	glFlush();
}
void reshape(int w, int h) {
	glViewport(0, 0, w, h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	if (w < h)
		gluOrtho2D(-200.0, 200.0, -200.0 * (float)h / (float)w, 200.0 * (float)h / (float)w);
	else
		gluOrtho2D(-200.0 * (float)w / (float)h, 200.0 * (float)w / (float)h, -200.0, 200.0);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
}

int main(int argc, char** argv) {
	

	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(500, 500);
	glutInitWindowPosition(100, 100);
	glutCreateWindow("Translation of Point, Line, and Triangle");

	init();

	glutDisplayFunc(display);
	glutReshapeFunc(reshape);
	glutMainLoop();
	return 0;
}