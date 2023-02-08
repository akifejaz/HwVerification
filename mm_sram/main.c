#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int * converNumtoBin(int num, int len){
    int * bin = (int *)malloc(len * sizeof(int));
    int i = 0;
    while(num > 0){
        bin[i] = num % 2;
        num = num / 2;
        i++;
    }
    return bin;
}

int main () {
    char * str = "Hello World";
    int len = strlen(str);

    printf("Length of string is %d \n", len);

    char * inpStr ; size_t l = 0;
    printf("Enter a string: ");
    getline(&inpStr, &l, stdin);

    printf("You entered: %s", inpStr);

    len = strlen(inpStr);
    printf("Length of string is %d \n", len);

    int * bin = converNumtoBin(10, 4);
    for(int i = 0; i < 4; i++){
        printf("%d", bin[i]);
    }

    // free the memory
    free(bin);
}