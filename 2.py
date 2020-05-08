for i in range(int(input())):
    len,que=map(int,input().split())
    lst1=list(input())
    st=sorted(set(lst1))
    lst2=[]
    for el in st:
        lst2.append(lst1.count(el))
    for j in range(que):
        lim=int(input())
        lst3= [x - lim for x in lst2]
        print(sum(x for x in lst3 if x > 0) )
