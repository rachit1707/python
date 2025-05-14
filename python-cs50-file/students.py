students = []
with open("students.csv") as file: #by default the mode of the open file is read
    for line in file:
        name, house = line.rstrip().split(",")
        #print(f"{name} is in {house}")
        #storing data in dict
        student = {"name":name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]        

for student in sorted(students, key=get_name):
    print(f"{student['name']} belongs to house {student['house']}")

#you can also use lambda for sorting as below
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student["name"]} belongs to house {student["house"]}")                