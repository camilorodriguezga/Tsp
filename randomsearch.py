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

class RandomSearch(object):
	"""docstring for Tsp"""
	def __init__(self):
		super(RandomSearch, self).__init__()
		"""on plane coordinate"""
		plt.ion()

	def buildRoute(self):
		print "init date: " + str(date.datetime.now())
		#init solution
		d, coorR = self.generateRandomSolution(coor)

		k=1
		while k < n:
			dt, rs =self.generateRandomSolution(coor)
			if dt<d:
				d=dt
				coorR = rs
				Tsp().drawTsp(coorR[:,0], coorR[:,1], d)
			k = k+1

		#print date end
		print "end date: " + str(date.datetime.now())

	def generateRandomSolution(self, coordinate):
		newCoor = cp.copy(coor)
		coorR = [newCoor.pop(0)]
		dt = 0
		while newCoor:
			pos = self.getRandomCoordinate(newCoor)
			p2 = newCoor.pop(pos)
			d = Tsp().getDistance(coorR[-1], p2)
			dt += d
			coorR.append(p2)

		dt += Tsp().getDistance(p2, coorR[0])
		coorR.append(coorR[0])
		coorR = np.array(coorR)
		return dt, coorR

	def getRandomCoordinate(self, coordinate):
		return random.randint(0, len(coordinate)-1)

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
	RandomSearch().buildRoute()
	"""off plane coordinate"""
	plt.ioff()
	plt.show()