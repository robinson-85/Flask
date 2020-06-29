# como forma de aprendizagem podemos codificar assim:

def produto (nome):
    print (f"Produto: {nome} - R$ 2 K")

print ("Bem vindo ao meu site")
produto ("Cadeira Gamer")
print ("Copyright - 2020")   

print ("Bem vindo ao meu site")
produto ("Teclado Mecânico")
print ("Copyright - 2020")

# Utilizando o decorator

def header(f):
    def decorator(*args, **kwargs):
        print("###Bem vindo ao meu site###")
        print("")
        return f(*args, **kwargs)
    return decorator

def footer(f):
    def decorator(*args, **kwargs):
        print("### Copyright - 2020 ###\n")
        return f(*args, **kwargs)
    return decorator

@footer
@header
def produto(nome, *kwargs):
    print(f"Produto: {nome} - R$ 2K")

@footer
@header
def sobre ():
    print ("Esta é a minha loja... conta:")    

produto ("Cadeira Gamer")
produto ("Teclado Mecânico")

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
                


