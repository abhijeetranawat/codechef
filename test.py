for h in range(int(input())):
    n=int(input())
    lst1 = sorted(list(map(int, input().split())))
    lst2 = sorted(list(map(int, input().split())))
    count=0
    for el in lst2:
        for ele in lst1:
            if(ele>el):
                count+=1
                lst1.remove(ele)
                break
    print(count)


    for el in lst2:
        if(lst1[0]>el):
            count+=1
            lst1.pop(0)
    print(count)