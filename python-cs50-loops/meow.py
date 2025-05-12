def main():
    while True:
        x = int(input("How much Meows? "))
        if x <= 0:
            continue
        else:
            break
    meow(x)

def meow(x):
    for _ in range(x):
        print("Meow")

main()        