class siblings:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def old(self):
        print(f"{self.name} is {self.age} years old!")
        
    def young(self):
        print(f"{self.name} is {self.age} years young!")

my_second_siblings = siblings("Aldrich", "19")

my_first_siblings = siblings("Hadrian", "21")

my_second_siblings.old()
my_first_siblings.young()