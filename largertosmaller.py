xx1=int(input())
ss1=list(map(int,input().split()))
yy1=sorted(ss1)[::-1]
zz1=""
if(ss1==[0]*xx1):
    print("0")
else:
    for j in yy1:
        zz1=zz1+str(j)
    print(int(zz1))
