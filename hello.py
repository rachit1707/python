name = input("What's your name:").strip() #strip is used to remove whitespaces from the start and end of the string

first, last = name.split(" ")

print(f"hello, {name}") #print with a format
print(f"hello, {first}") #prints the first name in the string