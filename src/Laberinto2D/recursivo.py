import numpy
from numpy.random import random_integers as rand
from random import randrange
import matplotlib.pyplot as pyplot
from time import sleep
import MazeExit
from pila import *

N = int(raw_input("ingresa orden de la matriz:"))
Y=[None]*N
for i in range(N): 
	Y[i]=[None]*N
X, Abajo, Arriba = MazeExit.maze(N,N)
#while((Y[0][Arriba] != Y[0][0]) or (Y[0][Arriba] != Y[0][N-1]) and ((Y[N-1][Abajo] != Y[N-1][0]) or (Y[N-1][Abajo] != Y[N-1][N-1]))):
#	X, Abajo, Arriba = MazeExit.maze(N-1,N-1)	
for i in range(N):
	for j in range(N):
		if X[i][j] == True:
			Y[i][j]=1
		else:
			Y[i][j]=0			
Y[0][Arriba]=3
			  
def search(x, y, p1):
		if Y[x][y] == 3:
			print 'Encontrado en %d,%d' % (y, x)
			print 'con la siguiente pila:'
			print p1.items
			return True
		elif Y[x][y] == 1:
			print 'Pared en %d,%d' % (y, x)
			p1.desapilar()
			return False
		elif Y[x][y] == 2:
			print 'Se visito %d,%d' % (y, x)
			p1.apilar("[%d,%d]" % (y, x))
			return False
		print 'Visitando %d,%d' % (y, x)
		# mark as visited
		Y[x][y] = 2
		if((x < len(Y)-1) or (y > 0) or(x > 0) or(y < len(Y)-1)):
			p1.apilar("[%d,%d]" % (y, x))
		#sleep(0.01)
		# explore neighbors clockwise starting by the one on the right
		if((x < len(Y)-1 and search(x+1, y, p1))
		or(y > 0 and search(x, y-1, p1))
		or(x > 0 and search(x-1, y, p1))
		or(y < len(Y)-1 and search(x, y+1,p1))):
			return True
		return False

def main():
	p1=Pila()
	search(N-1, Abajo, p1)
	pyplot.figure(figsize=(10, 5))
	pyplot.imshow(Y, cmap=pyplot.cm.binary, interpolation='nearest')
	pyplot.xticks([]), pyplot.yticks([])
	pyplot.draw();
	pyplot.show();
if __name__ == '__main__':
    main()

