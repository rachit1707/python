def main():
    print(f"Value returned is: {get_int("What's X? ")}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            #print("Value should be Integer")
            pass
main()        