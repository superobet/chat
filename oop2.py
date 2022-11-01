class animals:
    def breath(self):
        print(self.name + "Can breath")


class bird(animals):
    def __init__(self, name, age, description):
        self.name = name
        self.age = age
        self.description = description

    def fly(self):
        print(self.name + " Can fly")

    def sing(self):
        print(self.name + " Can sing")


class crocodile(animals):
    def __init__(self, name, age, description):
        self.name = name
        self.age = age
        self.description = description

    def bite(self):
        print(self.name + " Can bite")


flippy = bird("Flippy", 32, "red")
flippy.fly()
flippy.sing()
flippy.breath()
zelen = crocodile("Gena", 12, "red")
zelen.bite()
zelen.breath()
