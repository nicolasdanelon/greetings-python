class SayHi:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return "Greeting I'm {name}, emissary of the Gorgonites".format(name=self.name)

