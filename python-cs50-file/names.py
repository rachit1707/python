
name = input("What's the name? ")

with open("name.txt", "a") as file:
    file.write(f"{name}\n")