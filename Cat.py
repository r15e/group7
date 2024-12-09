from Animal import Animal

class Cat(Animal):
    def __init__(self):
        super().__init__()
        print("A cat has been created.")

    def meow(self):
        print("Meow!")