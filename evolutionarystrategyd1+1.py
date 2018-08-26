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

  def __init__(self):
  	super(EvolutionaryStrategy, self).__init__()
  	"""on plane coordinate"""
  	plt.ion()
  
  def buildRoute(self):
  	print "init date: " + str(date.datetime.now())
  	newCoor = cp.copy(coor)
  	coorR = [newCoor.pop(0)]
  	drt = dF = posF = coorF = dS = posS = coorS = 0
  	
  	while newCoor:
	  # generate solution father
	  dF, posF, coooF = self.generateFather(coorR[-1], newCoor)
	  coorF = newCoor.pop(posF)
	  # generate solution son
	  if len(newCoor) > 0:
	  	dS, posS, coorS = self.generateMutation(coorF, newCoor)
	  	coorS = newCoor.pop(posS)
	  else:
	  	dS = 0
	  # evaluate best solution and added coordinate
	  if dS<dF:
	  	drt += dS
	  	coorR.append(coorS)
	  	newCoor.insert(posF, coorF)
	  else:
	  	drt += dF
	  	coorR.append(coorF)
	  	if dS<>0:
	  		newCoor.insert(posS, coorS)
	  cd = np.array(coorR)
  	  Tsp().drawTsp(cd[:,0], cd[:,1], drt)
  
  	# connect endpoint with initial
  	drt += Tsp().getDistance(coorR[-1], coorR[0])
  	coorR.append(coorR[0])
  	coorR = np.array(coorR)
  	# draw solution
  	cd = np.array(coorR)
  	Tsp().drawTsp(cd[:,0], cd[:,1], drt)
  	print "end date: " + str(date.datetime.now())
  
  
  def generateMutation(self, coorF, coordinate):
  	coorS = [0,0]
  	dMin, pMin, cMin = self.nearestNeighbors([0,0], coor)
  	dMax, pMax, cMax = self.fartherNeighbors(cMin, coor)
  	distanceTotal = dMax - dMin
  	gm = distanceTotal * 0.01
  	coorS[0] = coorF[0] + ( gm * random.randint(-1, 1) )
  	coorS[1] = coorF[1] + ( gm * random.randint(-1, 1) )
  	return self.nearestNeighbors(coorS, coordinate)
  
  def generateFather(self, coorR, coordinate):
  	ncm =  cp.copy(coordinate)
  	p = c = dgf = N =0
  	if len(ncm)<3:
  	  N = 1
  	else:
  	  N = random.randint(1, 3)
  		
  	for i in range(0,N):
  	  dgf, p, c = self.nearestNeighbors(coorR, ncm)
  	  ncm.pop(p)
  	return dgf, p, c
  
  def nearestNeighbors(self, p1, coor):
  	dnn = pos = -1
  	i = 0
  	for item in coor[:]:
	  dTemp = Tsp().getDistance(p1, item)
	  if dnn == -1 or dTemp < dnn:
	  	dnn = dTemp
	  	pos = i
	  i += 1
  	return dnn, pos, coor[pos]
  
  def fartherNeighbors(self, p1, coor):
  	dfn = pos = -1
  	i = 0
  	for item in coor[:]:
	  dTemp = Tsp().getDistance(p1, item)
	  if dfn == -1 or dTemp > dfn:
	  	dfn = dTemp
	  	pos = i
	  i += 1
  	return dfn, pos, coor[pos]

if __name__ == '__main__':
	# init parameter
	nameFile = "data/test.tsp"
	n=1000
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