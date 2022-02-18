class Mood:
    def __init__(self):
        self.name = ""

    def getString(self):
        self.name = input()

    def printString(self):
        print(self.name.upper())

something = Mood()
something.getString()
something.printString()