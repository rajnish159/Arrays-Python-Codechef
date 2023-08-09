# cook your dish here
t = int(input())
for i in range(t):
    n,k = map(int, input().split())
    l = list(map(int, input().split()))
    m = 0
    for i in range(n-k+1):
        s = sum(l[i:i+k])
        m = max(m,s)
    print(m)
