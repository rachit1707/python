import sys

if len(sys.argv) < 2:
    sys.exit("Too few argument")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

for arg in sys.argv[1:-1]:  #this is the way to create a slice
        print("hello, my name is,", arg)        