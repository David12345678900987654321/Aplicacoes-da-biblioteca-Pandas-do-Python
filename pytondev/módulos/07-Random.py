import random

#1 escolher dados aleatórios de uma lista

lista = ["David","Luís","Leite"]
print(random.choice(lista))

#2 gerar número aleatórios
r=random.randint(0,15)
print(r)

#3 Seleciona mais de um valor aleatório
#random.sample(sequência, tamanho)

print(random.sample(lista,2))