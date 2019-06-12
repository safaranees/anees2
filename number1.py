n=int(input())
l,r=input().split()
l=int(l)
r=int(r)
b1=0
for i in range(l,r):
  if(i==n):
    b1=1
if(b1==1):
  print('yes')
else:
  print('no') 

 
