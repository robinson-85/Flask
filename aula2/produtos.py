class Categoria:
    def__init__(self, nome):
        self.nome = nome 


class Produto:
    def__init__(self, nome,categoria):
        self.nome = nome 
        self.categoria = categoria

cadeira = Produto("Cadeira", categoria=Categoria("Moveis"))
teclado = Produto("HiperX", categoria=Categoria("Eletronico"))
