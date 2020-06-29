#void

def ola():
    print("Olá")

    ola()

# funcao retorno

def soma (a: int, b: int)-> int:
    resultado = a+b
    return resultado

result = soma (5, 5)
print(result)   

# header (cabecalho) and footer(rodape)

def mensagem (header, footer):
    print(header)
    print("Olá você está no CodeShow")
    print(footer)

mensagem(header = "###inicio###", footer = "###fim###")   

# Para a funcao ficar mais legivel utiliza-se

def mensagem (header, footer):
    header()
    print("Olá você está no CodeShow")
    footer()

def header():
    print("###inicio")

def footer():
    print("###fim")


mensagem (header = header, footer = footer)