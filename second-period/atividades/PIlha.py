#PIlha
#LIFO

def criarPilha():
    pilha = []
    return pilha

def verificarVazio(pilha):
    return len(pilha) == 0

#Empilhar
def push(pilha, item):
    pilha.append(item)

#desempilhar
def pop(pilha):
    if not verificarVazio(pilha):
        return pilha.pop()
    else:
        return "A pilha está vazia, não é possivel tirar elementos"

#topo
def peek(pilha):
    if not verificarVazio(pilha):
        return pilha[-1]
    else:
        return "A pilha está vazia, não é possivel ver o topo"

#tamanho
def size(pilha):
    return len(pilha)

pilha = criarPilha()

push(pilha, 1)
push(pilha, 2)
push(pilha, 3)

#print(peek(pilha))

#print(pop(pilha))
#print(pop(pilha))

push(pilha,13)

#print(pop(pilha))

nomes = criarPilha()

push(nomes, "Arlindo")
push(nomes, "Renato")
push(nomes, "Enzo")
push(nomes, "Valentina")

#print(pop(nomes))
#print(pop(nomes))
#print(pop(nomes))
#print(pop(nomes))

#print(verificarVazio(nomes))
#print(pop(nomes))

#print(size(pilha))
#print(size(nomes))

