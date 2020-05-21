n=int(input())
lst1=list(map(int,input().split()))
lst2=list(map(int,input().split()))
lst3=[]
for i in range(n):
    lst3.append(lst2[i]//lst1[i])
print(min(lst3))