n, k = map(int, input().split())
target = [str(i) for i in range(1, n+1)]
pointer = 0
answer = []

while target:
    pointer = (pointer+k-1)%len(target)
    answer.append(target.pop(pointer))

print("<"+", ".join(answer)+">")