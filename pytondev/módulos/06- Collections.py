from collections import Counter,namedtuple,deque
from operator import itemgetter

#1 contagem de intens iguais
frutas= ["Maça","Banana","Banana","Laranja"]
print(Counter(frutas))

#2 Tuplas nomeadas
jogo = namedtuple("jogo",["nome","preço","nota"])
J1 = jogo("Mario",100,10.5)
print(J1)

#3 ordenando dicionários
estudantes = {"Nome1": "David", "Nome2": "Luís", "Nome3": "Leite"}
a=sorted(estudantes.items(), key=itemgetter(0))
"""
sorted(item a ser ordenado,
o elemento a ser utilizado como parâmetro para ser ordenado,
se vai ser em ordem crescente ou decrescente
sorted(variável,key=,reverse=true/false)
)
"""
print(a)

#4 deque é uma lista em que é mais eficiente de se adicionar elementos no início ou fim
deq= deque([20,40,60,80])
deq.appendleft(10)
print(deq)
deq.append(90)
deq.popleft()
print(deq)
