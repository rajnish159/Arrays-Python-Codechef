# cook your dish here
T = int(input())
for i in range(T):
    L, R = map(int, input().split())
    count = 0
    for i in range(L, R+1):
        if i%10 in(2,3,9):
            count += 1
    print(count)
            
            
