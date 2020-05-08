for i in range(int(input())):
    a=int(input())
    lst1=list(map(int,input().split()))
    lst2=[]
    n=1
    for j in range(1,a):
        if(lst1[j]-lst1[j-1]<=2):
            n=n+1
        else:
            lst2.append(n)
            n=1
    lst2.append(n)
    print(min(lst2),max(lst2))