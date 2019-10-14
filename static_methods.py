class StaticExample:

    def __init__(self):
        print("This is a static method example class")

    @staticmethod
    def example_function():
        print("I am a static method")


example = StaticExample.example_function()
