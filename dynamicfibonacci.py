res=[1,2]


def func(n):
    for i in range(len(res), n + 1):
        res.append((res[i - 1] + res[i - 2]))


for i in range(int(input())):
    n = int(input()) - 1
    if(len(res)<n):
        func(n)
    print(res[n])