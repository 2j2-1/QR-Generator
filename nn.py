import random
import numpy as np
from utils import *
def train(inputs, outputs):
	x = np.array(inputs)
	y = np.array(outputs)
	syn0 = 2*np.random.random((x.shape[1],x.shape[0])) - 1
	syn1 = 2*np.random.random((y.shape[0],y.shape[1])) - 1
	j = 00
	l2_error = y

	while np.mean(np.abs(l2_error))>0.005:
		j+=1
		l0 = x
		l1 = nonlin(np.dot(l0, syn0))
		l2 = nonlin(np.dot(l1, syn1))

		l2_error = y-l2

		if j%10000==0:
			print "Error:" + str(np.mean(np.abs(l2_error)))
		l2_delta = l2_error*nonlin(l2, deriv=True)

		l1_error = l2_delta.dot(syn1.T)

		l1_delta = l1_error*nonlin(l1, deriv=True)

		syn1 += l1.T.dot(l2_delta)
		syn0 += l0.T.dot(l1_delta)
	return [syn0,syn1]

def accruacy(inputs,outputs):
	inputs = inputs[:]
	outputs = outputs[:]
	inputs,outputs = shuffle_list(inputs,outputs)
	testingDataInput, traingDataInput = split_list(inputs,0.1)
	expectedDataOutput, traingDataOutput = split_list(outputs,0.1)

	syn = train(traingDataInput,traingDataOutput)
	testingDataOutput = test(syn,testingDataInput)
	stats = pair(testingDataOutput , expectedDataOutput)
	print str(len(testingDataOutput)) , "Record Used for testing"
	return stats,syn
	

inputs=[list_to_character_codes("COMP10081_19244 : 10/10/2017 16:00, JOC006"),
		list_to_character_codes("COMP10081_19244 : 12/10/2017 12:00, MAE206"),
		list_to_character_codes("COMP10081_19244 : 12/10/2017 16:00, MAE203"),
		list_to_character_codes("BIOL14406_25654 : 12/10/2017 16:00, JOC006"),
		list_to_character_codes("COMP10081_19244 : 12/10/2017 17:00, JOC006"),
		list_to_character_codes("COMP10081_19244 : 13/10/2017 15:00, MAE119"),
		list_to_character_codes("COMP10081_19244 : 16/10/2017 09:00, MAE119"),
		list_to_character_codes("SOFT30121_1198* : 16/10/2017 13:00, NHBLTB"),
		list_to_character_codes("SOFT30121_1198* : 16/10/2017 16:00, ERC196"),
		list_to_character_codes("COMP30201_3468* : 16/10/2017 15:00, ABK012"),
		list_to_character_codes("COMP10081_19244 : 17/10/2017 10:00, MAE202"),
		list_to_character_codes("COMP10081_19244 : 17/10/2017 11:00, MAE019"),
		list_to_character_codes("COMP10081_19244 : 16/10/2017 13:00, MAE205")
		]

outputs =  [list_to_character_codes("3730504467"),
			list_to_character_codes("2704566472"),
			list_to_character_codes("3499333079"),
			list_to_character_codes("2721726138"),
			list_to_character_codes("3073964699"),
			list_to_character_codes("3199571001"),
			list_to_character_codes("2000203501"),
			list_to_character_codes("2089713466"),
			list_to_character_codes("2089713466"),
			list_to_character_codes("177382910*"),
			list_to_character_codes("3088715953"),
			list_to_character_codes("3896539083"),
			list_to_character_codes("683658291*"),]


stats,syn = accruacy(inputs,outputs)
compare(stats)
percentage(stats)

use(syn,list_to_character_codes("COMP10081_19244 : 16/10/2017 16:00, MAE215"))
try:
	plot(inputs,outputs)
except:
	pass