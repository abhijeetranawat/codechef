import math
def pf(n):
    lst=[]
    while n%2==0:
        lst.append(2)
        n=n/2
    for k in range(3,int(math.sqrt(n))+1,2):
        while(n%k==0):
            lst.append(k)
            n=n/k
    if(n>2):
        lst.append(int(n))
    return list(set(lst))


for i in range(int(input())):
    count=0
    x,y,m=map(int,input().split())
    hcf=math.gcd(x,y)
    lstox=pf(x)
    lstoy=pf(y)
    lstox=[el for el in lstox if el<m]
    lstoy = [el for el in lstoy if el < m]
    lstox=sorted(lstox)
    lstoy = sorted(lstoy)
    facx=x/hcf
    facy=y/hcf
    while facx != 1:
        for el in lstox:
            if (facx % el == 0):
                facx = facx / el
                count += 1
                break
    while facy != 1:
        for el in lstoy:
            if (facy % el == 0):
                facy = facy / el
                count += 1
                break
    print(count, hcf)

