#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define STACK_SIZE 100

// Function to perform shift operation
void shift(char stack[], char input[], int *stackTop, int *inputPtr) {
    stack[++(*stackTop)] = input[(*inputPtr)++];
}

// Function to perform reduce operation
void reduce(char stack[], int *stackTop, char production[]) {
    int reduceLen = strlen(production) - 1;
    (*stackTop) -= reduceLen;

    // Perform reduction by popping reduceLen number of symbols from the stack
    printf("Reducing by production: %s\n", production);
    stack[++(*stackTop)] = production[0];
}

// Function to perform shift-reduce parsing
void shiftReduceParser(char input[]) {
    char stack[STACK_SIZE];
    int stackTop = -1;
    int inputPtr = 0;

    stack[++stackTop] = '$'; // Initial stack symbol
    printf("Stack\t\tInput\t\tAction\n");
    printf("-----\t\t-----\t\t------\n");
    printf("%s\t\t%s\t\t--\n", stack, input);

    while (input[inputPtr] != '\0') {
        stack[++stackTop] = input[inputPtr++];
        printf("%s\t\t%s\t\tShift\n", stack, input + inputPtr);

        // Check if reduction is possible
        if (stack[stackTop] == 'd' && stack[stackTop - 1] == 'S' && stack[stackTop - 2] == '+'
            && stack[stackTop - 3] == 'S' && stack[stackTop - 4] == '+') {
            reduce(stack, &stackTop, "S->S+S");
        } else if (stack[stackTop] == 'd' && stack[stackTop - 1] == 'S' && stack[stackTop - 2] == '*'
                   && stack[stackTop - 3] == 'S' && stack[stackTop - 4] == '*') {
            reduce(stack, &stackTop, "S->S*S");
        } else if (stack[stackTop] == 'd') {
            reduce(stack, &stackTop, "S->id");
        }
    }

    printf("%s\t\t%s\t\tAccept\n", stack, input + inputPtr);
}

int main() {
    char input[STACK_SIZE];
    printf("Enter the input string: ");
    scanf("%s", input);
    strcat(input, "$");

    shiftReduceParser(input);

    return 0;
}

