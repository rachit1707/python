names = [] #for storing and sorting the name read from the file

with open("name.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello,{name}")        