def main():
    x = int(input("What's X?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(x):
    return x % 2 == 0 #another way 'return True is x % 2==0 else False'
    
main()    
