import csv

students = []

with open("studentCsv.csv") as file:
    reader = csv.reader(file)
    for name, house in reader:
        students.append({"name":name, "house":house})

for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student["name"]} live in {student["house"]}")        