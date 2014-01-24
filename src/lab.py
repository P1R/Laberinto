import numpy
from numpy.random import random_integers as rand
#import matplotlib.pyplot as pyplot
 
def maze(width=80, height=50, complexity=1, density=1):
    # Only odd shapes
    shape = ((height // 2) * 2 + 1, (width // 2) * 2 +1)
    # Adjust complexity and density relative to maze size
    complexity = int(complexity * (5 * (shape[0] + shape[1])))
    density    = int(density * (shape[0] // 2 * shape[1] // 2))
    # Build actual maze
    Z = numpy.zeros(shape, dtype=bool)
    # Fill borders
    Z[0, :] = Z[-1, :] = 1
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
                if Z[y_, x_] == 0:
                    Z[y_, x_] = 1
                    Z[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 1
                    x, y = x_, y_
    return Z
''' 
z=maze(23,21)
worldMap=[None]*21
for i in range(21):
	worldMap[i]=[None]*23

i=0
for i in range(21):
	for j in range(23):
		if z[i][j] != False:
			worldMap[i][j]=2
		else:
			worldMap[i][j]=0	
print z
print worldMap

pyplot.figure(figsize=(10, 5))
pyplot.imshow(z, cmap=pyplot.cm.binary, interpolation='nearest')
pyplot.xticks([]), pyplot.yticks([])
pyplot.show()
'''