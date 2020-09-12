class Person:

    def __init__(self, name, age, gender):
        """
        Estes são atributos da classe
        """
        self.name = name
        self.age = age
        self.gender = gender

    """
    Estes são comportamentos das classes (métodos)
    """
    def introduce_yourself(self):
        print(f"Hi, I'm {self.name}, I'm {self.age} old and I'm a {self.gender}!")

    def walk(self):
        print(f"I'm just walking")

    def run(self):
        print(f"I'm just running")

    def eat(self):
        print(f"I'm just running eating")

if __name__ == '__main__':
    robinson = Person("Robinson", 35, "Masculino")
    rafael = Person("Rafael", 31, "Masculino")


    lista_de_pessoas = [robinson, rafael]

    for pessoa in lista_de_pessoas:
        pessoa.introduce_yourself()
        pessoa.walk()
        pessoa.run()
        pessoa.eat()
        print("\n")
