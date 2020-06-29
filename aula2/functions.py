# Funções

def ola (nome, cpf, idade=0, maiusculo = False, *args, **kwargs):

    print(args)
    print(kwargs)

    if maiusculo:
        msg = f"Olá, {nome}".upper()
    else:
            msg = f"Olá, {nome}, {cpf}, idade: {idade}"

            print(msg)

ola("Grad!", "12333340510")
ola("Karla!","12333340510", maiusculo = True)
ola("Lysandro","12333340510")

# Lista

pessoa = ['Karla', '4589456-45', 15] #banco de dados

ola(*pessoa)

# Dicionário

pessoa = {
    'nome': 'Karla', 
    'cpf':'4589456-45', 
    'idade':15
}

ola(**pessoa)


