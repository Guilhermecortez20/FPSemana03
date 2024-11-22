from collections import deque

palavras = input(" ").split()

fila = deque(reversed(palavras))

print(f"{fila}")

for palavra in fila:
    if 'a' in palavra:  
        print(palavra)

