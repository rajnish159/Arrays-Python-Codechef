# cook your dish here
T = int(input())
for i in range(T):
    N = int(input())
    l = []
    for i in range(N):
        l.append(int(input()))
    for i in l:
        if l.count(i)%2==1:
            print(i)
            break 

