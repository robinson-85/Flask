#Listas
#...........0.........1........2....
cores = ["vermelho","verde", "azul"]
numeros = [1,2,3]
mistura = [1, "robinson", 4.5, True, cores, numeros, [1,2,3]]
cores.append ("Amarelo")
cores.insert(1, "branco")
cores.remove ("azul") 

print(cores)


#Tuplas
#................0...........1...........2
identidade = ("Robinson", "398457555-2", 35)

print(f"nome é {identidade[0]}")
print(f"cpf é {identidade[1]}")
print(f"idade é {identidade[2]}")

#desempacotamento
nome, cpf, idade = identidade
print(nome, cpf, idade)

#dicionario(Array associativo, Hashmap, Object)
pessoa = {"nome": "Robinson", "cpf": "398457555-2", "idade": 35}

#para facilitar a leitura é mais fácil fazer assim:
pessoa = {
    "nome": "Karla",
    "cpf": "398457555-2", 
    "idade": 18
}
#se eu quiser mudar o dicionário posso fazer assim:

pessoa ["idade"] = 19
pessoa ["Canal"] = "@KarlaMag"

print(f"Olá, a {pessoa['nome']} tem {pessoa['idade']} anos")
