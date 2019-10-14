class Example:

    def __init__(self):
        print("This is a static method example class")

    @classmethod
    def class_example_function(cls):
        print("I am a class method")
        cls.static_example_function()

    @staticmethod
    def static_example_function():
        print("I am a static method")


example = Example()
example.class_example_function()

