from Animal import Animal

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("A dog has been created.")

    def bark(self):
        print("Woof!")