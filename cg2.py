
for h in range(int(input())):
    n=int(input())
    lst1 = list(map(int, input().split()))
    lst1.sort(reverse=True)
    lst2 = list(map(int, input().split()))
    lst2.sort(reverse=True)
    count=0
    f=0
    for el in lst2:
        if(lst1[f]>el):
            count+=1
            f+=1
    print(count)