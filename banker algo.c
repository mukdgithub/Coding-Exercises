#include <stdio.h>
#define MAX_PROCESSES 10
#define MAX_RESOURCES 10

int main() {
    int num_processes, num_resources, i, j, k;

    // Enter the number of processes and resources
    printf("Enter the number of processes: ");
    scanf("%d", &num_processes);
    printf("Enter the number of resources: ");
    scanf("%d", &num_resources);

    int available[MAX_RESOURCES];
    int max_claim[MAX_PROCESSES][MAX_RESOURCES];
    int allocation[MAX_PROCESSES][MAX_RESOURCES];
    int need[MAX_PROCESSES][MAX_RESOURCES];
    int finish[MAX_PROCESSES];

    // Enter the available resources
    printf("Enter the available resources:\n");
    for (i = 0; i < num_resources; i++) {
        printf("Resource %d: ", i + 1);
        scanf("%d", &available[i]);
    }

    // Enter the maximum claim of each process
    printf("Enter the maximum claim of each process:\n");
    for (i = 0; i < num_processes; i++) {
        printf("Process %d:\n", i + 1);
        for (j = 0; j < num_resources; j++) {
            printf("Resource %d: ", j + 1);
            scanf("%d", &max_claim[i][j]);
        }
    }

    // Enter the allocation matrix
    printf("Enter the allocation matrix:\n");
    for (i = 0; i < num_processes; i++) {
        printf("Process %d:\n", i + 1);
        for (j = 0; j < num_resources; j++) {
            printf("Resource %d: ", j + 1);
            scanf("%d", &allocation[i][j]);
            need[i][j] = max_claim[i][j] - allocation[i][j];
        }
        finish[i] = 0;
    }

    // Banker's algorithm
    int work[MAX_RESOURCES];
    int safe_sequence[MAX_PROCESSES];
    int safe_count = 0;

    for (i = 0; i < num_resources; i++) {
        work[i] = available[i];
    }

    int found;
    do {
        found = 0;
        for (i = 0; i < num_processes; i++) {
            if (finish[i] == 0) {
                int can_execute = 1;
                for (j = 0; j < num_resources; j++) {
                    if (need[i][j] > work[j]) {
                        can_execute = 0;
                        break;
                    }
                }

                if (can_execute) {
                    for (k = 0; k < num_resources; k++) {
                        work[k] += allocation[i][k];
                    }
                    finish[i] = 1;
                    safe_sequence[safe_count++] = i;

                    found = 1;
                }
            }
        }
    } while (found);

    // Check if the system is in a safe state
    int is_safe = 1;
    for (i = 0; i < num_processes; i++) {
        if (finish[i] == 0) {
            is_safe = 0;
            break;
        }
    }

    // Print the safe sequence if it exists
    if (is_safe) {
        printf("System is in a safe state.\nSafe sequence: ");
        for (i = 0; i < num_processes; i++) {
            printf("%d ", safe_sequence[i]);
        }
        printf("\n");
    } else {
        printf("System is not in a safe state.\n");
    }

    return 0;
}

