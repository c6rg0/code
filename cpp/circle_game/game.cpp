#include <raylib.h>
#include <iostream>
#include <random>
using namespace std;

int ball_x;
int ball_y;
int points;

int rand_ball_x_pos(int ball_x){
	random_device rd;
	mt19937 gen(rd());
	uniform_int_distribution<> dis(1,1230);
	ball_x = dis(gen);
	return ball_x;
}

int rand_ball_y_pos(int ball_y){
	random_device rd;
	mt19937 gen(rd());
	uniform_int_distribution<> dis(1,670);
	ball_y = dis(gen);
	return ball_y;
}

int main()
{
	InitWindow(1280, 720, "circle game");

	Vector2 ballposition = {(float)rand_ball_x_pos(ball_x),(float)rand_ball_y_pos(ball_y) };

	while (!WindowShouldClose())
	{
		BeginDrawing();

			ClearBackground(BLACK);
			DrawCircleV(ballposition, 50, WHITE);
			DrawText((string(points)), 640, 370, 25, WHITE)

		EndDrawing();

		if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON)){
			DrawCircleV(ballposition, 50, BLACK);
			ballposition = {(float)rand_ball_x_pos(ball_x),(float)rand_ball_y_pos(ball_y) };
			int points = points + 1;
		}


	}

	CloseWindow();
	return 0;

}

