import csv

name = input("What's you name: ")
house = input("What's your house: ")

with open("studentCsv.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, house])