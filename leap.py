yr=int(input())
if ((yr%400==0) or (yr%4==0) or (yr%100!=0)):
    print("Yes")
else:
    print("No")
