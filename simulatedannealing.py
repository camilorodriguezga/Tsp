# Local library
from basefile import BaseFile
from tsp import Tsp
from nearestneighbors import NearestNeighbors

import datetime as date
import copy as cp
import matplotlib.pyplot as plt
import math as m
import numpy as np
import random
import sys

class SimulatedAnnealing(object):
	"""docstring for Tsp"""
	def __init__(self, n, tk, alpha, swap):
		super(SimulatedAnnealing, self).__init__()
		self.n = n
		self.tk = tk
		self.alpha = alpha
		self.swap = swap
		"""on plane coordinate"""
		plt.ion()

	def buildRoute(self):
		print "init date: ", date.datetime.now()
		newCoor = cp.copy(coor)
		dF, coorF = self.generateFather(newCoor)
		k=0
		while k < self.n:
			dS, coorS = self.generateMutation(dF, coorF)
			if dS<dF:
				dF=dS
				coorF = coorS
			else:
				pa = np.exp(-np.absolute(dF-dS)/self.tk)
				self.tk = self.tk * self.alpha
				ra = random.uniform(1, 0)
				if (ra < pa):
					dF=dS
					coorF = coorS

			copyCoor = cp.copy(coorF)
			copyDF = cp.copy(dF)
			"""conected last position coordinate with the firt"""
			copyCoor.append(copyCoor[0])
			cd = np.array(copyCoor)
			Tsp().drawTsp(cd[:,0], cd[:,1], copyDF)
			"""stop criteria"""
			k = k+1
		"""print final solution"""
		print "distance: ", dF, "coordinates: ", coorF
		print "end date: ", date.datetime.now()


	def generateFather(self, coordinate):
		coorR = [coordinate.pop(0)]
		dt = 0
		while coordinate:
			d, position, p2 = NearestNeighbors().nearestNeighbors(coorR[-1], coordinate)
			dt += d
			coorR.append(p2)

		dt += Tsp().getDistance(coorR[-1], coorR[0])
		return dt, coorR

	def generateMutation(self, dF, coorF):
		coorSon = cp.copy(coorF)
		dsnew = dfnew = dsold = dfold = dson = 0
		posR = self.getRandomCoordinate(coorSon)
		swap = self.getPosSwap(coorF, posR)

		dspold, dsnold, dfpold, dfnold = self.getDistanceSwap(coorF, posR, swap)		

		temp = coorSon[posR]
		coorSon[posR] = coorSon[swap]
		coorSon[swap] = temp

		dspnew, dsnnew, dfpnew, dfnnew = self.getDistanceSwap(coorSon, posR, swap)
		dson = dF + (dspnew - dspold) + (dsnnew - dsnold) + (dfpnew - dfpold) + (dfnnew - dfnold)
		return dson, coorSon

	def getPosSwap(self, coorF, posR):
		s = posR + random.randint(-1*self.swap, self.swap)
		#validate borde in list coordinates
		if s > len(coorF) - 1:
			s = s - len(coorF)
		elif s < 0:
			s = len(coorF) + s
		return s

	def getDistanceSwap(self, coorF, posR, swap):
		dsprev = dsnext = drprev = drnext = 0

		posSNext = self.getNextPos(coorF, swap)
		posSPrev = self.getPrevPos(coorF, swap)
		posRNext = self.getNextPos(coorF, posR)
		posRPrev = self.getPrevPos(coorF, posR)

		dsnext = Tsp().getDistance(coorF[swap], coorF[posSNext])
		dsprev = Tsp().getDistance(coorF[swap], coorF[posSPrev])

		drnext = Tsp().getDistance(coorF[posR], coorF[posRNext])
		drprev = Tsp().getDistance(coorF[posR], coorF[posRPrev])

		return dsprev, dsnext, drprev, drnext

	def getNextPos(self, coorF, pos):
		posNext = pos + 1
		if posNext > len(coorF) - 1:
			posNext = posNext - len(coorF)
		return posNext

	def getPrevPos(self, coorF, pos):
		posPrev = pos - 1
		if posPrev < 0:
			posPrev = len(coorF) + posPrev
		return posPrev

	def getRandomCoordinate(self, coordinate):
		return random.randint(0, len(coordinate)-1)

if __name__ == '__main__':
	# init parameter
	nameFile = "data/berlin52.tsp"
	n=100
	tk = 100
	alpha = 0.86
	swap = 2
	# get input data
	if len(sys.argv) > 1:
		nameFile = "data/" + sys.argv[1]
	if len(sys.argv) > 2:
		n = int(sys.argv[2])
	if len(sys.argv) > 3:
		tk = int(sys.argv[3])
	if len(sys.argv) > 4:
		alpha = float(sys.argv[4])
	if len(sys.argv) > 5:
		swap = int(sys.argv[5])
	# get coordinate
	coor = BaseFile().getContent(nameFile)
	SimulatedAnnealing(n,tk,alpha,swap).buildRoute()
	"""off plane coordinate"""
	plt.ioff()
	plt.show()