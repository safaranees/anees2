str1=input()
a1=[]
b1=[]
for i in range(0,len(str1)):
    if i%2==0:
        a1.append(str1[i])
    else:
        b1.append(str1[i])
for i in range(0,len(str1)//2):
    print(b1[i],end="")    
    print(a1[i],end="")
