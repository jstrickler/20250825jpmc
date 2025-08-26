colors = []   #  JAVA: list colors = new list();
# colors = list()
colors.append("red")

value = 5   # int value = int(5);
print(f"{type(value) = }")

class Dog:  # CamelCase StudlyCaps
    def bark(self):   #  JAVA: 'this'
        print("Woof! Woof!")

    def multibark(self, count):
        print("Woof! " * count)

d1 = Dog()
d2 = Dog()
print(f"{d1 = }")
d1.bark()
d1.multibark(5)
# Dog.multibark(d1, 5) 