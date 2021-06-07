#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int main(int argc, char *argv[])
{
    srand((unsigned int)time(NULL));
    int point_circle = 0;
    int point_total = atoi(argv[1]);
    for (int i = 0; i < point_total; i++)
    {
        float x = -1 + rand() / (float) RAND_MAX *2;
        float y = -1 + rand() / (float) RAND_MAX *2;
        if (x*x + y*y <= 1) point_circle++;
    }
    float pi = (float) 4*point_circle/point_total;
    printf("%f\n", pi);
    return 0;
}