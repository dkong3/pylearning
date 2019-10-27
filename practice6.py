def ranking(x):
    if x<100:
        print ("given number is smaller than 100")
    elif x>=100 and x<1000:
        print("given number is between 100 and 1000")
    elif x>=1000 and x<2000:
        print("given number is between 1000 and 2000")
    else:
        print("given number is larger than 2000")

num=float(input("type a number"))

ranking(num)