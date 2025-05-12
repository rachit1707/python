def main():
    print_col(3)
    print_row(4)

def print_col(height):
    for _ in range(height):
        print("#")

def print_row(width):
    print("#" * width)        

main()
