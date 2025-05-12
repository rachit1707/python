#lists understanding
students = ["Hermoine", "Ron", "Harry"]

for student in students:
    print(student)

for i in range(len(students)):
    print(students[i])   


#dict understanding
wizzards = {
    "Hermoine":"Gryffindor",
    "Ron":"Gryffindor",
    "Harry":"Gryffindor",
    "Draco":"Slytherin"
}

for wizzard in  wizzards:
    print(wizzard, wizzards[wizzard], sep=",")

#list of dict
wizzardList = [
    {"name":"Hermoine", "house":"Gryffindor"},
    {"name":"Ron", "house":"Gryffindor"},
    {"name":"Harry", "house":"Gryffindor"},
    {"name":"Draco", "house":"Slytherin"}
]

for wizzar in wizzardList:
    print(wizzar["name"], wizzar["house"], sep="-")