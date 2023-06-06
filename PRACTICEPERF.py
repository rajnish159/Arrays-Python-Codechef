# cook your dish here
P1,P2,P3,P4 = map(int, input().split())
if P1>=10 and P2>=10 and P3>=10 and P4>=10:
    print("4")
elif P1>=10 and P2>=10 and P3>=10:
    print("3")
elif P1>=10 and P2>=10:
    print("2")
elif P1>=10:
    print('1')
else:
    print("0")
    
