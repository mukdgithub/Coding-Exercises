#include <stdio.h>
#include <stdbool.h>
#define MAX_FRAMES 3
#define MAX_PAGES 10
typedef struct {
int page;
int time;
} Frame;
int pages[MAX_PAGES];
Frame frames[MAX_FRAMES];
void initializeFrames() 
{
for(int i=0;i<MAX_FRAMES;i++) 
{
frames[i].page = -1;
frames[i].time = -1;
}
}
void printFrames() {
for (int i = 0; i < MAX_FRAMES; i++) {
if (frames[i].page == -1) {
printf("-");
} else {
printf("%d", frames[i].page);
}
printf("\t");
}
printf("\n");
}
void fifo() {
int faults = 0;
int frameIndex = 0;
initializeFrames();
 for (int i = 0; i < MAX_PAGES; i++) {
int page = pages[i];
bool pageFault = true;
for (int j = 0; j < MAX_FRAMES; j++) {
if (frames[j].page == page) {
pageFault = false;
break;
}
}
if (pageFault) {
faults++;
frames[frameIndex].page = page;
frameIndex = (frameIndex + 1) % MAX_FRAMES;
}
printf("Page %d:\t", page);
printFrames();
}
printf("FIFO Page Faults: %d\n\n", faults);
}
void lru() {
int faults = 0;
int frameIndex = 0;
initializeFrames();
for (int i = 0; i < MAX_PAGES; i++) {
int page = pages[i];
bool pageFault = true;
int oldestTime = frames[0].time;
int oldestIndex = 0;
for (int j = 0; j < MAX_FRAMES; j++) {
if (frames[j].page == page) {
pageFault = false;
frames[j].time = i;
break;
}
if (frames[j].time < oldestTime) {
oldestTime = frames[j].time;
 oldestIndex = j;
}
}
if (pageFault) {
faults++;
frames[oldestIndex].page = page;
frames[oldestIndex].time = i;
}
printf("Page %d:\t", page);
printFrames();
}
printf("LRU Page Faults: %d\n\n", faults);
}
int findOptimal(int start) {
int farthest = start;
int maxIndex = -1;
for (int i = 0; i < MAX_FRAMES; i++) {
int page = frames[i].page;
bool found = false;
for (int j = start + 1; j < MAX_PAGES; j++) {
if (page == pages[j]) {
found = true;
if (j > farthest) {
farthest = j;
maxIndex = i;
}
break;
}
}
if (!found) {
maxIndex = i;
break;
}
}
return maxIndex;
}
void optimal() {
int faults = 0;
initializeFrames();
for (int i = 0; i < MAX_PAGES; i++) {
int page = pages[i];
bool pageFault = true;
for (int j = 0; j < MAX_FRAMES; j++) {
if (frames[j].page == page) {
pageFault = false;
break;
}
}
if (pageFault) {
faults++;
int replaceIndex = findOptimal(i);
frames[replaceIndex].page = page;
}
printf("Page %d:\t", page);
printFrames();
}
printf("Optimal Page Faults: %d\n\n", faults);
}
int main() {
printf("Page Replacement Algorithms Simulation\n\n");
printf("Enter the page reference string (separated by spaces):\n");
for (int i = 0; i < MAX_PAGES; i++) {
scanf("%d", &pages[i]);
}
printf("\n");
fifo();
lru();
optimal();
return 0;
}
