#include <raylib>
#include <iostream>

using namespace std;

string turn = "X";
string winner = "";
bool run = True;
bool draw = False;
bool game = True;
bool is_terminal = False;
int turn_number = 0;
double score = 0;


void drawXO(row, col, turn);
void is_terminal(node);
void minimax(node, depth, maximizingPlayer);
void get_children(node, player);
void heuristic_value(node);
void find_best_move();
void validation(grid, is_terminal);
void announcment(is_terminal, winner, draw);


int main(){
	
	initwindow(900,900, "naughts and crosses");
	
	while(!windowshouldclose()){
		begindrawing();
			clearbackground(grey);
			if IsMouseButtonPressed(MOUSEBUTTON){
				mx = GetMouseX();
				my = GetMouseY();
				row
		enddrawing();
	}

	closewindow();
	return 0;
}


