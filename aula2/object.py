class Animal:
    # atributos de classe
    planeta = "Terra"
    animal_nasceu = False

    def nasceu(self):
        return self.animal_nasceu

    # metodo
    def nascer(self):
        self.animal_nasceu = True
        print(f"Oi, eu nasci na {self.planeta}")

    def comer(self):
        print("Estou comendo...crunch crunch")

class Mamifero(Animal):

    def comer(self):
        print("Estou tomando leite...")

class Oviparos(Animal):

    def nascer(self):
        print(f"Acabei de quebrar o ovo no planeta {self.planeta}")

class Especial(Mamifero, Oviparos):

    def nadar(self):
        print("Tchibummmmmm")

# a class acima é chamada de heranca dupla, mas, nao é um bom uso.





