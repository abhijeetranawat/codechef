for i in range(int(input())):
    x,y,le,r=map(int,input().split())
    if(x==0 or y==0):
        print(0)
        break
    lst1=[]
    for j in range(le, r+1):
        lst1.append((x & j) * (y & j))
    mx=max(lst1)
    for k in range(len(lst1)):
        if(lst1[k]==mx):
            print(k+le)
            break
