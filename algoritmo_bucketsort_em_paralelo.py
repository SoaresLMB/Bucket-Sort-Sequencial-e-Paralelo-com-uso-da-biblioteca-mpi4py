import math
from mpi4py import MPI
import random

comunicador = MPI.COMM_WORLD
my_rank = comunicador.Get_rank()
p = comunicador.Get_size()

tempo_inicial = MPI.Wtime()

random.seed(77)
array = random.sample(range(1,50000000),20000000)
n_baldes = p-1
valor_max_array = max(array)
v =valor_max_array/n_baldes

MAXBALDE = math.ceil(v)

array_enviado = None
if my_rank == 0:
    array_enviado = array

array_recebido = comunicador.bcast(array_enviado,root=0)

balde = []

if my_rank != 0:
    for j in array_recebido:

        if my_rank == 1:
            valor_max_balde = math.ceil(v)
            valor_min_balde = 0
            if j >= valor_min_balde and j < valor_max_balde:
                balde.append(j)
        else:
            valor_min_balde = MAXBALDE * (my_rank - 1)
            valor_max_balde = valor_min_balde + MAXBALDE
            if j >= valor_min_balde and j < valor_max_balde:
                balde.append(j)
                
    for z in range(n_baldes):
        balde = sorted(balde)

arrays = comunicador.gather(balde,root=0)

if my_rank == 0:
    print(arrays)
    array_ordenado = []
    for lista in arrays:
        for i in lista:
            array_ordenado.append(i)
    print(f'array ordenado: {array_ordenado}')

    tempo_final = MPI.Wtime()
    tempo_decorrido = tempo_final - tempo_inicial
    tempo_decorrido_min = tempo_decorrido / 60
    print(f'O tempo decorrido foi: {tempo_decorrido} segundos')
    print(f'O tempo decorrido foi: {tempo_decorrido_min} minutos')

MPI.Finalize()






