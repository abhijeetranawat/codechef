for i in range(int(input())):
    x,y,m=map(int,input().split())
    lstprime=[]
    for num in range(2, m):
        if all(num % i != 0 for i in range(2, num)):
            lstprime.append(num)
    lst1=[]
    lst2=[]
    for el in lstprime:
        if(el<x):
            a=x
            while(a%el==0):
                a=a/el
                lst1.append(int(a))
        else:
            break
    for el in lstprime:
        if(el<y):
            a=y
            while(a%el==0):
                a=a/el
                lst2.append(int(a))
        else:
            break
    lst1=sorted(lst1)
    lst2 = sorted(lst2)
    for h in range(len(lst1)):
        if lst1[h] in lst2:
            k = h
    print(lst1[k])