for i in range(int(input())):
    str=list(input().split(":"))
    hr=int(str[0])
    if(hr>9):
        st={1,2,3,4,5}
    else:
        st={0,1,2,3,4,5}
    hrst="{}".format(hr)
    st1=set(hrst)
    print(st1)
    st=st-st1
    print(st)