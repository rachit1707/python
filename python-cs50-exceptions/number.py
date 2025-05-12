while True:
    try:
        x = int(input("What's X? "))
    except ValueError:
        print("Value is not Integer")
    else:
        break

print(f"Value of X is {x}")            