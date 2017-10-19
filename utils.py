import random
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
def list_to_character_codes(string):
	l = list(string)
	newList = []
	for i in l:
		newList.append(ord(i)/100.0)
	return newList

def nonlin(x,deriv=False):
	if deriv==True:
		return (x*(1-x))

	return 1/(1+np.exp(-x))

def shuffle_list(ins,outs):
	newins = []
	newouts = []
	for i in range(len(ins)):
		randomPos=random.randint(0,len(ins)-1)
		newins.append(ins[randomPos])
		newouts.append(outs[randomPos])
		del ins[randomPos]
		del outs[randomPos]
	return newins,newouts

def split_list(l, percentage):
	return l[:int(round(len(l)*percentage))],l[int(round(len(l)*percentage)):]

def pair(l1,l2):
	values = []
	for i in range(len(l1)):
		for j in range(len(l1[i])):
			values.append((round(l1[i][j]*100),round(l2[i][j]*100)))
	return values 

def compare(l):
	sum = 0
	for i in l:
		if i[0] == i[1]:
			sum+=1
	sum/=float(len(l))
	print "Perfect Match:", str(int(sum*100)) + "% Accurate"

def percentage(l):
	values = []
	for i in l:
		values.append(100 - abs((i[1]-i[0])/i[1]*100))
	print "Values:",str(sum(values)/len(values))+"% Accurate"

def test(syn,inputs):
	l0 = inputs
	l1 = nonlin(np.dot(l0, syn[0]))
	l2 = nonlin(np.dot(l1, syn[1]))

	return l2

def use(syn,String):

	l0 = [String]
	l1 = nonlin(np.dot(l0, syn[0]))
	l2 = nonlin(np.dot(l1, syn[1]))

	print l2


	print_ascii_code(l2,String)
def print_ascii_code(l2,String):
	string = ""
	for i in l2[0]:
		print i,int(round(i*100)),chr(int(round(i*100)))
		string += chr(int(round(i*100)))
	print "String:", String ,"\nProduced Code:",
	print string 

def plot(x1,y1):

	# Create a trace
	trace = go.Scatter(
	    x = x1,
	    y = y1
	)

	data = [trace]

	py.iplot(data, filename='basic-line')