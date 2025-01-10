def func(target):
    s = 0
    for t in target:
        if t == ")":
            if s > 0:
                s -= 1
            else:
                return "NO"
        else:
            s += 1
    
    if s > 0:
        return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    print(func(input()))