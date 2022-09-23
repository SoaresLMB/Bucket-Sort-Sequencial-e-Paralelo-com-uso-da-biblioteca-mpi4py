import numpy as np
import math
from mpi4py import MPI
import random

tempo_inicial = MPI.Wtime()

random.seed(77)
array = random.sample(range(1,200000),100000)
n_baldes = 3
valor_max_array = np.amax(array)
v =valor_max_array/n_baldes

MAXBALDE = math.ceil(v)

balde = []

# Create empty buckets
for k in range(n_baldes):
    balde.append([])

for j in array:
    valor_max_balde = math.ceil(v)
    valor_min_balde = 0

    for i in range(n_baldes):
        if j >= valor_min_balde and j <= valor_max_balde:
            balde[i].append(j)
            i=0
            break
        else:
            valor_min_balde = valor_max_balde
            valor_max_balde += MAXBALDE
            
for z in range(n_baldes):
    balde[z] = sorted(balde[z])

array_ordenado = []

for k in range(n_baldes):
    for d in balde[k]:
        array_ordenado.append(d)

print(f'Array em ordem crescente:{array_ordenado}')

tempo_final = MPI.Wtime()
tempo_decorrido = tempo_final - tempo_inicial
tempo_decorrido_min = tempo_decorrido/60
print(f'O tempo decorrido foi: {tempo_decorrido} segundos')
print(f'O tempo decorrido foi: {tempo_decorrido_min} minutos')
