# cook your dish here
T = int(input())
for i in range(T):
    n = int(input())
    l = list(map(int, input().split()))
    print(len(set(l)))
   
