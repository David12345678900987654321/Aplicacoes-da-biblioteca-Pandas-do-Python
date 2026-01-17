"""
Args é utilizado quando não se sabe quantos paâmetros serão passados
os argumentos são passados como uma tupla
Kwargs é utilizado para passar também as chaves para cada argumentos
os argumentos são passados como um dicionário
"""
def soma (*num):
    soma = 0
    for n in num:
        soma= soma+n
    return soma
print(soma(7,9,4))

def indentidade (**dados):
    for key, values in dados.items():
        print(f"{key}  {values}")
print("indentificação")
indentidade(nome = "David", idade = 19)