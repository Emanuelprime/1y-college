#Inserção - no final
def enqueue(fila, elemento):
    fila.append(elemento)
#Remoção - no inicio
def dequeue(fila):
    if len(fila) == 0:
        return "A fila está vazia, não é possível remover"
    else:
        return fila.pop(0)

#Primeiro elemento - peek
def peek(fila):
    if len(fila) == 0:
        return "Fila vazia"
    else:
        return fila[0]
def is_empty(fila):
    return len(fila) == 0

def size(fila):
    return len(fila)
"""Desafio: Uma pessoa está em uma fila de um parque de diversões e deseja saber qual é o tempo de espera estimado para
chegar ao brinquedo. Cada pessoa leva um determinado tempo para utilizar o brinquedo e, em seguida, sai da fila. 
A pessoa quer saber qual será a sua posição na fila e quanto tempo ela terá que esperar para chegar no brinquedo"""

fila = ['person1',"person2","person3"]

tempoEstimado = 5
for i in range(input())


