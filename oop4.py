class person:
    def __init__(self, name, age, eyes):
        self.__name = name

        self.age = age
        self.eyes = eyes

    def __work(self):
        print(self.__name + " can do his job")

    def registration(self):
        def __part1():
            print("Hollow on my program, who do your want to be? ")
            type_of_person = input("Worker/Boss?")
            if type_of_person == "Worker" or type_of_person == "Boss" or type_of_person == "worker" or type_of_person == "boss":
                __part2()
            else:
                print("Repeat 1 more time")
                __part1()

        def __part2():
            user_login = input("Enter login")
            user_password = input("Enter password")
            self.__user_login = user_login
            self.__user_password = user_password
            with open("text.txt", "a") as file:
                file.write(user_login + " " + user_password + "\n")

            print("succsesful registration!")

        __part1()

    def login(self):
        login = input("Enter your login ")
        password = input("Enter your password ")
        with open("text.txt") as file:
            for i in file.readlines():
                saved_login = i.split()[0]
                saved_password = i.split()[1]
                if saved_login == login and saved_password == password:
                    print("Welcome to system!")
                    return True
            print("NO welcome to system")


class worker(person):
    def __init__(self, name, age, eyes):
        super().__init__(name, age, eyes)

    def work(self):
        print(self.__name + " can do his job")


class boss(person):
    def __init__(self, name, age, eyes):
        super().__init__(name, age, eyes)

    def work(self):
        print(self.name + " can argue")


worker1 = worker("Vasilii", "32", "brown")
boss1 = boss("Afanasijs", "73", "grey")

person1 = person("Arkadii", "21", "blue")
person1._person__work()
person1.login()
