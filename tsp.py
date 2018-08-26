import matplotlib.pyplot as plt
import math as m
import numpy as np
import sys
import datetime as date

from basefile import BaseFile

class Tsp(object):
	"""docstring for Tsp"""
  def __init__(self):
  	super(Tsp, self).__init__()
  	"""on plane coordinate"""
  	plt.ion()
  
  def drawTsp(self, x, y, dt):
  	plt.cla()
  	"""scatter set point in the cordenates x,y"""
  	plt.scatter(x[:], y[:], s=100, c='k')
  	"""beeline with coordinate x, y"""
  	plt.plot(x, y, 'r-')
  	"""show text in coordinate plane"""
  	plt.text(-max(x)/10, -max(x)/10, "Total distance=%.2f" % dt, fontdict={'size': 12, 'color': 'green'})
  	"""draw coordinate plane with x between -0.1,4 and y -0.1,4"""
  	plt.xlim((-max(x)/10, max(x)+(max(x)/10)))
  	plt.ylim((-max(x)/10, max(y)+(max(x)/10)))
  	plt.pause(0.01)
  
  def getDistance(self, p1, p2):
  	return m.hypot(p2[0] - p1[0], p2[1] - p1[1])
