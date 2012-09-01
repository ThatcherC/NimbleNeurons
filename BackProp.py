#!/usr/bin/python

#variables------------------------------------------------
structure = [4,2,4]
maxIns = 4
weights = list(range((structure[1]+structure[2])*maxIns))

setOne = [1,0,1,0]
setTwo = [0,1,0,1]
setThree = [1,1,0,0]
setFour = [0,0,1,1]

outOne = [0,0]
outTwo = [0,1]
outThree = [1,0]
outFour = [1,1]

#functions------------------------------------------------

def setup():				#setup weights, globals
	print 'go'

def train(l, tget, neuron):					#trains one neuron (l is training set + target
	global a,weights,y,target
	a = 0								#important - reinitialize
	target = tget
	for i in range(len(l)):
		a = a+(l[i]*weights[i+(numins*neuron)])#-thetas[neuron]	#adds weights times inputs
	y = activate(a)							#squashes
	for i in range(len(l)):
		weights[i+(numins*neuron)] += modifyWeight(l[i])

def evaluateNeuron(e, neuron):
	global a,weights,y
	a=0;								#important - reinitialize
	for i in range(len(e)):
		a = a+(e[i]*weights[i+(numins*neuron)])#-thetas[neuron]	#adds weights times inputs
		
	y = activate(a)							#squashes
	return y

def evaluateNet(inList):
	if len(inList) != structure[0]:
		return "Input data doesn't match structure"
	else:
		interList = []
		for i in range(structure[1]):
			interList.insert(0,evaluateNeuron(inList, structure[1]-i-1))
		print interList
		outputList = []
		for i in range(structure[1], structure[1]+structure[2]):
			outputList.insert(0,evaluateNeuron(interList, (structure[2]+structure[1]+1)-i))
		return outputList

def modifyWeight(inn):
	return alpha*(target-y)*inn*dactivate(a)


def activate(x):
	return 1/(1+(2.71828**(0-x)))

def dactivate(x):
	return (activate(x+0.01)-activate(x-0.01))/.02
