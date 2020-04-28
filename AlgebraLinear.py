from random import randint, seed

def determinante(matriz): #Limitada a 2x2
    tamanho = len(matriz)
    diagonalPrincipal = 1
    diagonalSecundaria = 1
    for i in range(tamanho):
        diagonalPrincipal *= matriz[i][i]
    x = 0
    y = tamanho-1
    while x < tamanho:
        diagonalSecundaria *= matriz[x][y]
        x += 1
        y -= 1
    return diagonalPrincipal - diagonalSecundaria

def criarMatriz(linhas, colunas):
    matriz = [[0 for coluna in range(colunas)] for linha in range(linhas)] #Cria N colunas para cada M linhas
    for linha in range(linhas):
        for coluna in range(colunas):
            matriz[linha][coluna] = randint(1, 10)
    return matriz

def multiplicaMatriz(A, B):
    C = [[0 for linha in range(len(A))] for coluna in range(len(B[0]))] #Cria M linhas para cada N colunas
    for linhaA in range(len(A)):
       for coluna in range(len(B[0])):
           for linhaB in range(len(B)):
               C[linhaA][coluna] += A[linhaA][linhaB] * B[linhaB][coluna]
    return C

seed(0)
A = criarMatriz(2, 3)
B = criarMatriz(3, 2)
C = multiplicaMatriz(A, B)
print(A)
print(B)
print(C)
D = criarMatriz(2,2)
print(D)
print(determinante(D))
