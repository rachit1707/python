def main():
    x = int(input("What's X? "))
    print("x squared is:",square(x))  

def square(x):
    return pow(x, 2)    #we can also do x**2 or x*x


main()      