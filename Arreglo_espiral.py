import math
tamano = int(input("Ingrese el tamaño del cuadrado: "))

arreglo = [[0] * tamano for _ in range(tamano)]
def espiral(arreglo):
    direccion = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direc_actual = 0 
    f_ini = 0
    f_fin = tamano - 1
    col_ini = 0
    col_fin = tamano - 1
    cont = 1

    while f_ini <= f_fin and col_ini <= col_fin:
        if direc_actual == 0:
            for i in range(col_ini, col_fin + 1):
                arreglo[f_ini][i] = cont
                cont += 1
            f_ini += 1
        elif direc_actual == 1:
            for i in range(f_ini, f_fin + 1):
                arreglo[i][col_fin] = cont
                cont += 1
            col_fin -= 1
        elif direc_actual == 2:
            for i in range(col_fin, col_ini - 1, -1):
                arreglo[f_fin][i] = cont
                cont += 1
            f_fin -= 1
        elif direc_actual == 3:
            for i in range(f_fin, f_ini - 1, -1):
                arreglo[i][col_ini] = cont
                cont += 1
            col_ini += 1

        direc_actual = (direc_actual + 1) % 4
    for fila in arreglo:
        for e in fila:
            print(e, end=' ')
        print()
espiral(arreglo)
print("El tamaño del cuadrado es :",tamano)
