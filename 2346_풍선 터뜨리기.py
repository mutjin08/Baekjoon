n = int(input())
papers = list(map(int, input().split()))

from collections import deque
balloons = [i for i in range(1, n+1)] #balloons
pointer = 0 #pointer

while len(balloons)>1:
    target = balloons.pop(pointer) - 1
    pointer = (pointer + papers[target])%len(balloons)
    print(pointer, balloons)
