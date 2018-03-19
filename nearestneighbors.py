# Local library
from basefile import BaseFile
from tsp import Tsp

import datetime as date
import matplotlib.pyplot as plt
import numpy as np
import sys

class NearestNeighbors(object):
	"""docstring for Tsp"""
	def __init__(self):
		super(NearestNeighbors, self).__init__()
		"""on plane coordinate"""
		plt.ion()

	def buildRoute(self):
		print "init date: " + str(date.datetime.now())
		coorR = [coor.pop(0)]
		dt = 0
		while coor:
			d, position, p2 = self.nearestNeighbors(coorR[-1], coor)
			dt += d
			coorR.append(p2)
			cd = np.array(coorR)
			Tsp().drawTsp(cd[:,0], cd[:,1], dt)

		dt += Tsp().getDistance(p2, coorR[0])
		coorR.append(coorR[0])
		cd = np.array(coorR)
		Tsp().drawTsp(cd[:,0], cd[:,1], dt)
		print "end date: " + str(date.datetime.now())
		
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

if __name__ == '__main__':
	nameFile = "data/test.tsp"
	if len(sys.argv) > 1:
		nameFile = "data/" + sys.argv[1]
	coor = BaseFile().getContent(nameFile)
	NearestNeighbors().buildRoute()
	"""off plane coordinate"""
	plt.ioff()
	plt.show()
