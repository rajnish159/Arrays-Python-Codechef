# cook your dish here
T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    a = list(map(int,input().split()))
    count = 0
    for i in range(N):
        if a[i]>K:
            count = count+1
      
    print(count)
        
        
    
