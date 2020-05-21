for i in range(int(input())):
    n,lim = map(int, input().split())
    lst1=list(map(int,input().split()))
    lst2=[]
    lst4=[]
    count=0
    for j in range(lim):
        for k in range(n):
            if(lst1[k]!=k+1):
                num1=lst1[k]
                lst2.append(num1)
                lst4.append(k)
            if(len(lst4)==3):
                break
        if(len(lst4)==3):
            lst1[lst4[0]]=lst2[2+j*3]
            lst1[lst4[1]] = lst2[0 + j * 3]
            lst1[lst4[2]] = lst2[1 + j * 3]
            lst4=[]
            count+=1
            lst3 = sorted(lst1)
            if (lst1 == lst3):
                break
        else:
            break

    lst3=sorted(lst1)
    if(lst1==lst3):
        print(count)
        h=0
        for v in range(len(lst2)//3):
            print(lst2[h+2],lst2[h],lst2[h+1])
            h+=3
            print("\n")
    else:
        print(-1)