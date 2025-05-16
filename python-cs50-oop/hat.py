import random

class Hat:
    houses = ["Gryffindor", "Huffelpuff", "Slytherin", "Ravenclaw"]

    @classmethod #similar to making method static in java
    def sort(cls, name):
        print(f"{name} belongs to house {random.choice(cls.houses)}")


Hat.sort("Harry")    