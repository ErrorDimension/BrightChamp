#include <stdio.h>

int main()
{
    int a, arr[100], i, j = 0, jump = 0;
    scanf("%d", &a);
    for (i = 0;i < a;i++) {
        scanf("%d", &arr[i]);
    }

    while (j < a) {
        if (arr[j + 2] == 0) {
            jump += 1;
            j += 2;
        }
        else {
            jump += 1;
            j += 1;
        }
    }
    printf("%d", jump - 1); // must minus 1 because the last jump counted
}

