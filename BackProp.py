#!/usr/bin/python

from random import *

#variables------------------------------------------------
structure = [4,2,4]						#structure of network - input, intermediate, outs
maxIns = 4							#greatest number of inputs for any neuron
weights = list(range((structure[1]+structure[2])*maxIns))
pweights = list(range(len(weights)))

setOne = [1,0,1,0]
setTwo = [0,1,0,1]
setThree = [1,1,0,0]
setFour = [0,0,1,1]

outOne = [0,0]
outTwo = [0,1]
outThree = [1,0]
outFour = [1,1]

alpha = 0

#functions------------------------------------------------

def setup():				#setup variables
	global alpha			#import globals to modify
	print 'go'
	alpha = 0.1

def train(l, tget, neuron):					#trains one neuron (l is training set + target
	global a,weights,y,target					#import globals
	a = 0								#important - reinitialize
	target = tget
	for i in range(len(l)):
		a = a+(l[i]*weights[i+(maxIns*neuron)])			#adds weights times inputs
	y = activate(a)							#squashes
	for i in range(len(l)):
		weights[i+(maxIns*neuron)] += modifyWeight(l[i])

def evaluateNeuron(e, neuron):
	global a,weights,y
	a=0;								#important - reinitialize
	for i in range(len(e)):
		a = a+(e[i]*weights[i+(maxIns*neuron)])#-thetas[neuron]	#adds weights times inputs
		
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

def activate(x):						#Activation function
	return 1/(1+(2.71828**(0-(x/4))))

def dactivate(x):						#Approximate derivative of the activation 
	return (activate(x+0.01)-activate(x-0.01))/.02		#function. Returns the slope of a certain point
	

#program----------------------------------------------------------

setup()
for p in range((structure[1]+structure[2])*maxIns):		#Initialize weights randomly
	weights[p] = random()
	pweights[p] = weights[p]				

#print weights							#Uncomment to print initial random weights

for m in range(20000):
	train(setOne,1, 0)					#Intermediary neuron 1
	train(setTwo,0, 0)
	train(setThree,1,0)
	train(setFour,0, 0)

	train(setOne,1, 1)					#Intermediary neuron 2
	train(setTwo,0, 1)
	train(setThree,0,1)
	train(setFour,1, 1)

	train(outOne,0,2)					#Target '1' output neuron
	train(outTwo,0,2)
	train(outThree,0,2)
	train(outFour,1,2)

	train(outOne,1,3)					#Target '2' output neuron
	train(outTwo,0,3)
	train(outThree,0,3)
	train(outFour,0,3)

	train(outOne,0,4)					#Target'3' output neuron
	train(outTwo,0,4)
	train(outThree,1,4)
	train(outFour,0,4)

	train(outOne,0,5)					#Target '4' output neuron
	train(outTwo,1,5)
	train(outThree,0,5)
	train(outFour,0,5)

for i in range(len(weights)):
	print pweights[i]-weights[i]

print evaluateNet(setOne)