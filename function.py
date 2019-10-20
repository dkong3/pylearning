
def fabi(n):
    a=0
    b=1
    if n<=0:
        print("given number is invalid")

    elif n==1:
        pass
    else:
        pass
        for i in range(2,n):
            c=a+b
            a=b
            b=c

            if c>100:
                print(a)
                break

fabi(100)
