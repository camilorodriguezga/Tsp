# Local library
from basefile import BaseFile
from tsp import Tsp

import datetime as date
import copy as cp
import matplotlib.pyplot as plt
import math as m
import numpy as np
import random
import sys

class EvolutionaryStrategy(object):
	"""docstring for Tsp"""
	def __init__(self):
		super(EvolutionaryStrategy, self).__init__()
		"""on plane coordinate"""
		plt.ion()

	def buildRoute(self):
		print "init date: " + str(date.datetime.now())
		newCoor = cp.copy(coor)
		coorR = [newCoor.pop(0)]
		dt = 0

		while newCoor:
			# generate solution father
			posP = self.generateRandomCoordinate(newCoor)
			coorP = newCoor[posP]
			dP = Tsp().getDistance(coorR[-1], coorP)
			# generate solution son
			posS = self.generateMutation(posP, newCoor)
			coorS = newCoor[posS]
			dS = Tsp().getDistance(coorR[-1], coorS)
			# evaluate best solution and added coordinate
			if dS<dP:
				dt += dS
				coorR.append(newCoor.pop(posS))
			else:
				dt += dP
				coorR.append(newCoor.pop(posP))
			# draw solution
			cd = np.array(coorR)
			Tsp().drawTsp(cd[:,0], cd[:,1], dt)

		# connect endpoint with initial
		dt += Tsp().getDistance(coorR[-1], coorR[0])
		coorR.append(coorR[0])
		coorR = np.array(coorR)
		# draw solution
		cd = np.array(coorR)
		Tsp().drawTsp(cd[:,0], cd[:,1], dt)
		print "end date: " + str(date.datetime.now())

	def generateRandomCoordinate(self, coordinate):
		return random.randint(0, len(coordinate)-1)

	def generateMutation(self, currentPosition, coordinate):
		nextPosition = currentPosition + random.randint(len(coordinate)/-5, len(coordinate)/5)
		if nextPosition > 0 and nextPosition < len(coordinate):
			return nextPosition
		else:
			return len(coordinate)-1

if __name__ == '__main__':
	# init parameter
	nameFile = "data/berlin52.tsp"
	n=100
	# get input data
	if len(sys.argv) > 1:
		nameFile = "data/" + sys.argv[1]
	if len(sys.argv) > 2:
		n = int(sys.argv[2])
	# get coordinate
	coor = BaseFile().getContent(nameFile)
	EvolutionaryStrategy().buildRoute()
	"""off plane coordinate"""
	plt.ioff()
	plt.show()