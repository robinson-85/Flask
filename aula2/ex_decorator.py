# exemplo de decorator simples

def pao (f):
    def wrapper(recheio):
        f(recheio)
    return wrapper

def lanche(recheio):
    print("(pao)")
    print(f"{recheio}")
    print("hamburguer")    

# posso simplificar o código

def pao(f):
    def wrapper():
        print("(fatia superior de pao)")
        f()
        print("(fatia inferior de pao)")
    return wrapper

@pao
def x_vegan():
    print("hamburguer vegano")

@pao
def opa():
    print("  ")

x_vegan()
opa()
