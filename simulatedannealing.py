# Local library
from basefile import BaseFile
from tsp import Tsp
from nearestneighbors import NearestNeighbors
from evolutionarystrategy import EvolutionaryStrategy

import datetime as date
import copy as cp
import matplotlib.pyplot as plt
import math as m
import numpy as np
import random
import sys

class SimulatedAnnealing(object):

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
  	dF, coorF = EvolutionaryStrategy(self.n, self.swap).generateFather(newCoor)
  	k=1
  	while k < self.n:
	  dS, coorS = EvolutionaryStrategy(self.n, self.swap).generateMutation(dF, coorF)
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