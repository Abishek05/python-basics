class Dog:
    kind = 'canine'
    # tricks = []

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


my_dog = Dog('Carl')
my_dog.add_trick('roll over')

another_dog = Dog('Max')
another_dog.add_trick('play dead')

print(my_dog.name, my_dog.kind, my_dog.tricks)
print(another_dog.name, another_dog.kind, another_dog.tricks)

