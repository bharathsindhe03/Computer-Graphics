// 2D transformation without using Built-in 
#include<iostream>
#include<GL/glut.h>
#include<stdlib.h>
#include<stdio.h>

float tx = 0, ty = 0, sx = 1, sy = 1, angle = 0;

float vertices[3][2] = {
	{0.0, 0.5},
	{-0.5, -0.5},
	{0.5, -0.5}
};

void init()
{
	glClearColor(0.0, 0.0, 0.0, 1.0);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(-1.0, 1.0, -1.0, 1.0);
	glMatrixMode(GL_MODELVIEW);
}

void display()
{
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(1.0, 0.0, 0.0);
	glBegin(GL_TRIANGLES);
	for (int i = 0; i < 3; i++) {
		float x = vertices[i][0];
		float y = vertices[i][1];

		x *= sx;
		y *= sy;

		float rad = angle * 3.142 / 180.0;
		float x_rot = x * cos(rad) - y * sin(rad);
		float y_rot = x * sin(rad) + y * cos(rad);
		x = x_rot;
		y = y_rot;

		x += tx;
		y += ty;
		glVertex2f(x, y);
	}
	glEnd();
	glFlush();
}

void keyboard(unsigned char key, int x, int y)
{
	switch (key)
	{
	case 'w': 
		ty += 0.1;
		break;
	case 's':
		ty -= 0.1;
		break;
	case 'a': 
		tx -= 0.1;
		break;
	case 'd':
		tx += 0.1;
		break;
	case '+':
		sx += 0.1;
		sy += 0.1;
		if (sx > 2.0)
			sx = 2.0;
		if (sy > 2.0)
			sy = 2.0;
		break;
	case '-':
		sx -= 0.1;
		sy -= 0.1;
		if (sx < 0.1)
			sx = 0.1;
		if (sy < 0.1)
			sy = 0.1;
		break;
	case 'r':
		angle -= 5.0;
		break;
	case 'l':
		angle += 5.0;
		break;
	case 27:
		exit(0);
	}
	glutPostRedisplay();
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(500, 500);
	glutInitWindowPosition(100, 100);
	glutCreateWindow("Program 2");
	init();
	glutDisplayFunc(display);
	glutKeyboardFunc(keyboard);
	glutMainLoop();
	return 0;
}