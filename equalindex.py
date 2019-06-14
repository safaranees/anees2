nn=int(input())
ll=[]
array=list(map(int,input().split()))
for x in range(0,nn):
    if(array[x]==x):
        ll.append(x)
if(len(ll)==0):
    print("-1")
ll.sort()
for x in ll:
    print(x,end=" ")
