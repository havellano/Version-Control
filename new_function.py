class siblings:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def old(self):
        print(f"{self.name} is {self.age} years old!")

my_siblings = siblings("Aldrich", "19")

my_siblings.old()
