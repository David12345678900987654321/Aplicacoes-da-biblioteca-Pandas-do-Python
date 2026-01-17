import re

texto = "muitos filmes"
#1 busca o índice inicial e final de palavras

match = re.search(r'muitos',texto)

print(f"índice incial: {match.start()}")
print(f"índice final: {match.end()}")

#2 busca de índice de um elemento específico

match = re.search(r'm',texto)
print(f"índice incial: {match}")

#3 busca lista de caracteres

letras = "[a-m]"
resultados = re.findall(letras,texto)

print(f"{resultados}")

#4 verificando o iníco de strings

rule = r'^A'
#cria uma regra em que a string só será considerada se começar com 
# A maiúsculo 
frases=['bom dia','A ilha do medo', 'a ilha do medo']

for i in frases:
    if re.match(rule, i):
        print(f"confirma {i}")
    else:
        print(f"não confirma {i}")
print("\n")

#5 verifica o final da string
rule = r'o$'
frasess=['bom dia','A ilha do medo', 'a ilha do medo']

for ii in frasess:
    if re.search(rule, ii):
        print(f"confirma {ii}")
    else:
        print(f"não confirma {ii}")