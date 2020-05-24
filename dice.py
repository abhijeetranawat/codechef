for i in range(int(input())):
    n = int(input())
    count = 0

    if (n % 12 == 0):
        print(n // 12)
        continue
    elif (n % 10 == 0):
        print(n // 10)
        continue
    elif (n < 12):
        print(-1)
        continue
    else:
        while (n % 12 != 0 and n > 12):
            n = n - 10
            count += 1
        count = count + (n // 12)

        if (n % 12 == 0):
            print(count)
        else:
            print(-1)