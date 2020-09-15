class Categoria:
    def __init__(self, nome):
        self.nome = nome 


class Produto:
    def __init__(self, nome,categoria):
        self.nome = nome 
        self.categoria = categoria

produto = Produto("Cadeira", categoria="Movel")

print(produto.publico)  # OK

print(produto._protegida)  # Ok (mas não recomendado)

print(produto.__privada)  # Error!!!

# Name mangling
print(produto._Produto__privada)  # Funciona mas não use a não ser para debug