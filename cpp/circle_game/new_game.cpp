#include <raylib.h>
#include <iostream>
#include <random>

using namespace std;

struct Circle {
	Vector2 position;
	float radius;
	Color color;
};

int main()
{
	int screen_width = 1280;
	int screen_height = 720;
	initwindow(screen_width, screen_height, "Basic ryhthm game");
	float ball_x;
	float ball_y;
	
	int scroll_speed = 0;
	int bpm = 0;
	int proccessed_bpm = bpm / 60;
	int total_notes = 0;

	while (!windowshouldclose())
	{
		/*
		if (isKeyDown(KEY_D));
		if (isKeyDown(KEY_F));
		if (isKeyDown(KEY_J));
		if (isKeyDown(KEY_K));
		*/
		
		
		
		begindrawing();
			clearbackground(black);
			drawcriclev(ballposition, 50, white);
		enddrawing();
	}
	closewindow();
	return 0;
}
