import matplotlib.pyplot as plt
import math as m
import numpy as np
import sys
import datetime as date

class BaseFile(object):
	def __init__(self):
		super(BaseFile, self).__init__()
	"""docstring for BaseFile"""
	def getContent(self, nameFile):
		content = open(nameFile)
		coor = []
		print content.readline()
		print content.readline()
		print content.readline()
		dimension = content.readline().split(" ")[1]
		print dimension
		print content.readline()
		print content.readline()
		count = 1
		with content as fp:
			for line in fp:
				if count <= int(dimension):
					data = line.split(" ")
					coor.append([float(data[1]), float(data[2])])
				count+=1
		print coor
		return coor

if __name__ == '__main__':
	nameFile = "data/berlin52.tsp"
	if len(sys.argv) > 1:
		nameFile = "data/" + sys.argv[1]
	coor = BaseFile().getContent(nameFile)
