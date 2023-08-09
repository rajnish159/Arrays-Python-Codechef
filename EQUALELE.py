# cook your dish here
from collections import Counter
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    c = Counter(arr)
    max_freq = max(c.values())
    print(n-max_freq)