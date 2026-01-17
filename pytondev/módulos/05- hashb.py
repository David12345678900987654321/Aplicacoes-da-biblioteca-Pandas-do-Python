import hashlib
#biblioteca de criptografia de dados

#1 verficando os algoritmos disponíveis

print(hashlib.algorithms_available)
print("\n")

#2 verficando os algoritmos disponíveis segundo o OS
print(hashlib.algorithms_guaranteed)

#3 SHA256
algoritomo = hashlib.sha256()
mensagem = "oi, como vai?".encode()
algoritomo.update(mensagem)
print(algoritomo.hexdigest())

#4 utilizando o MD5 (utilizado para verificar a integridade de dados)
"""
para verificar se um arquivo foi modificado você pode verificar o hash
"""