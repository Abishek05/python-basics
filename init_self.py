class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name


my_dog = Dog('Carl')
another_dog = Dog('Max')
print(my_dog.name, my_dog.kind)
print(another_dog.name, another_dog.kind)
