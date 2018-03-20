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

class SimulatedAnnealing(object):
	"""docstring for Tsp"""
	def __init__(self):
		super(SimulatedAnnealing, self).__init__()
		"""on plane coordinate"""
		plt.ion()

	def buildRoute(self):
		print "init date: " + str(date.datetime.now())
		tk = 100
		alpha = 0.98
		newCoor = cp.copy(coor)
		dF, coorF = self.generateFather(newCoor)
		k=1
		while k < n:
			dS, coorS = self.generateMutation(dF, coorF)

			if dS<dF:
				dF=dS
				coorF = coorS
			else:
				pa = np.exp(-np.absolute(dF-dS)/tk)
				tk = tk * alpha
				ra = random.uniform(1, 0)
				if (ra < pa):
					dF=dS
					coorF = coorS

			cd = np.array(coorF)
			Tsp().drawTsp(cd[:,0], cd[:,1], dF)
			k = k+1 

		print "end date: " + str(date.datetime.now())


	def generateFather(self, coordinate):
		coorR = [coordinate.pop(0)]
		dt = 0
		while coordinate:
			d, position, p2 = self.nearestNeighbors(coorR[-1], coordinate)
			dt += d
			coorR.append(p2)

		dt += Tsp().getDistance(p2, coorR[0])
		coorR.append(coorR[0])

		return dt, coorR
		
	def nearestNeighbors(self, p1, coor):
		d = -1
		pos = -1
		i = 0
		for item in coor[:]:
			dTemp = Tsp().getDistance(p1, item)
			if d == -1 or dTemp < d:
				d = dTemp
				pos = i
			i += 1
		
		return d, pos, coor.pop(pos)

	def generateMutation(self, dF, coorF):
		coorSon = cp.copy(coorF)
		dsnew = dfnew = dsold = dfold = dson = 0
		posR = self.getRandomCoordinate(coorSon)
		swap = posR + random.randint(-2, 2)
		if swap > 0 and swap < len(coorF) -1:
			dsold, dfold = self.getDistanceSwap(coorF, posR, swap)

			temp = coorSon[posR]
			coorSon[posR] = coorSon[swap]
			coorSon[swap] = temp

			dsnew, dfnew = self.getDistanceSwap(coorSon, posR, swap)

		dson = dF + (dsnew - dsold) + (dfnew - dfold)
		return dson, coorSon

	def getDistanceSwap(self, coorF, posR, swap):
		dnext = dprev = 0

		if swap > posR and swap < len(coorF) -1 and posR > 0:
			dnext = Tsp().getDistance(coorF[swap], coorF[swap + 1])
			dprev = Tsp().getDistance(coorF[posR], coorF[posR - 1])
		elif swap < posR and swap > 0 and posR < len(coorF) -1:
			dnext = Tsp().getDistance(coorF[swap], coorF[swap - 1])
			dprev = Tsp().getDistance(coorF[posR], coorF[posR + 1])
		return dnext, dprev

	def getRandomCoordinate(self, coordinate):
		return random.randint(0, len(coordinate)-1)

if __name__ == '__main__':
	# init parameter
	nameFile = "data/linhp318.tsp"
	n=20
	# get input data
	if len(sys.argv) > 1:
		nameFile = "data/" + sys.argv[1]
	if len(sys.argv) > 2:
		n = int(sys.argv[2])
	# get coordinate
	coor = BaseFile().getContent(nameFile)
	SimulatedAnnealing().buildRoute()
	"""off plane coordinate"""
	plt.ioff()
	plt.show()