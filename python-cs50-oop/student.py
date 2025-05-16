class Student:
    def __init__(self, name, house): #Constructor of the class
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} is from {self.house} house" 
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
    
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Red", "Yellow", "Blue", "Red"]:
            raise ValueError("Invalid House name")
        self._house = house

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ") 
        return cls(name, house)   

def main():
    student = Student.get()
    print(student)   

if __name__ == "__main__":
    main()     