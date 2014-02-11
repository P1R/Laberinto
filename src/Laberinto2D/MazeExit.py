import numpy
from numpy.random import random_integers as rand
from random import randrange
#import matplotlib.pyplot as pyplot
 
def maze(width=81, height=51, complexity=1, density=1):
    # Only odd shapes
    shape = ((height // 2) * 2 + 1, (width // 2) * 2 + 1)
    # Adjust complexity and density relative to maze size
    complexity = int(complexity * (5 * (shape[0] + shape[1])))
    density    = int(density * (shape[0] // 2 * shape[1] // 2))
    # Build actual maze
    Z = numpy.zeros(shape, dtype=bool)
    # Fill borders
    #Parte Superior
    Z[0, :] =1 
    #parte inferior
    Z[-1, :] = 1 
    #llenando laterales
    Z[:, 0] = Z[:, -1] = 1
    # Make isles
    for i in range(density):
        x, y = rand(0, shape[1] // 2) * 2, rand(0, shape[0] // 2) * 2
        Z[y, x] = 1
        for j in range(complexity):
            neighbours = []
            if x > 1:             neighbours.append((y, x - 2))
            if x < shape[1] - 2:  neighbours.append((y, x + 2))
            if y > 1:             neighbours.append((y - 2, x))
            if y < shape[0] - 2:  neighbours.append((y + 2, x))
            if len(neighbours):
                y_,x_ = neighbours[rand(0, len(neighbours) - 1)]
                if Z[y_, x_] == 0:#definir condiciones para no cubrir ni entrada ni salida
                    Z[y_, x_] = 1
                    Z[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 1
                    x, y = x_, y_
    #seleccion de salida aleatoria en la parte superior para final
    random_fin = randrange(1, len(Z[0,:])-1)
    Z[0,random_fin]=False
    #selecciona de entrada aleatoria en la parte inferior para inicio
    random_start = randrange(1, len(Z[-1,:])-1)
    Z[-1,random_start]=False 
    
    return Z, random_start, random_fin
