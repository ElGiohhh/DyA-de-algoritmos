#!/bin/python3/yo_merenges_-_-/

import math
import os
import random
import re
import sys

def simpleArraySum(ar):
    suma = 0
    for elemento in ar:
        suma += elemento
    return suma
    
if __name__ == '__main__':
    ar_count = int(input("Ingrese el tamaño del arreglo: ").strip())
    ar = []
    print("Ingrese los valores del arreglo, uno por uno:")
    for _ in range(ar_count):
        ar_item = int(input().strip())
        ar.append(ar_item)
    result = simpleArraySum(ar)
    print("La suma de los elementos del arreglo es:", result)
    result_ascii = str(result).encode('ascii', 'ignore').decode()
    with open("output.txt", "w") as fptr:
        fptr.write(result_ascii + '\n')