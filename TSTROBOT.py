t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    string = list(input())
    new = [x]
    for i in string:
        if i == "R":
            new.append(new[-1]+1)
        else:
            new.append(new[-1]-1)
    print(len(set(new)))
   