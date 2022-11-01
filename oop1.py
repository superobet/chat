class Person:
    def __init__(self, name, age, city):
        self.firstname = name
        self.age = age
        self.city = city
        print("Hello world!")
    def walk(self):
        print(self.firstname)
        print("I can walk!")
    def run(self):
        print("I can run!")
    def sleep(self):
        print("I can sleep!")


person = Person("Max", 20, "Kiev")
person.walk()
# person.sleep()
# person.run()
