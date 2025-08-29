#include <stdio.h>

typedef unsigned char byte;

enum {width=20, height=15};
byte image[width][height];

void display(void) {
	for (int y=0; y<height; ++y) {
		for (int x=0; x<width; ++x) {
			printf("%c ", (image[x][y]) ? 'x' : '-');
		}
		puts("");
	}
}

int main(void) {
	image[12][2]=1;
	display();
}
