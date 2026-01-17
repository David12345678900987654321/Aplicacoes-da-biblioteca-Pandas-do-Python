import statistics

#1 média
print(statistics.mean([2,3,4,5,6,7,8]))

#2 mediana
print(statistics.median([2,3,4,5,6]))
print(statistics.median([2,3,4,5,6,7]))

#3 moda
print(statistics.mode([2,3,4,5,2,6,7,2]))

#4 descio padrão

"""
quanto mais perto de zero for o desvio padrão, 
menos dispersos estão os dados
"""
print(statistics.stdev([1,2,3,4,5,6]))
