# cook your dish here
T = int(input())
for i in range(T):
    a = int(input())
    m = input()
    n = input()
    if m.count("1")==n.count("1")  and m.count("0")==n.count("0"):
        print("YES")
    else:
        print("NO")
