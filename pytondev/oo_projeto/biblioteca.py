class biblioteca:
    nome = ""
    ativo = False

biblioteca_cidade = biblioteca()
biblioteca_cidade.nome = "Biblioteca da cidade"
biblioteca_cidade.ativo = True

biblioteca_shopping = biblioteca()

print(vars(biblioteca_shopping))
print(vars(biblioteca_cidade),"\n")
#var faz o print imprimir o obejto da classe como um dicionário

bibliotecas = [biblioteca_cidade,biblioteca_shopping]

for biblioteca in bibliotecas:
    print(vars(biblioteca))