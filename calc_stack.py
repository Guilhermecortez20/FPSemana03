from collections import deque

entrada = input(" ")

numerous = list(map(int, entrada.split()))

pilha = deque(numerous)

print(pilha)

while pilha:
    elemento = pilha.pop()
    print(elemento * 2)
