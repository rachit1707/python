import sys

def main():
    if len(sys.argv) == 2:
        hello(sys.argv[1])
        goodbye(sys.argv[1])

def hello(name):
    print("hello", name)

def goodbye(name):
    print("goodbye", name)  

if __name__ == "__main__": #checks if the main method is called then will execute it or else will not execute it
    main()      