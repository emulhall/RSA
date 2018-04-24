import itertools
import Table
import Utterance
import PossibleWorld
import Rsa
import Speaker
import World
import InitialListener
import Listener
import matplotlib.pyplot as plt
import numpy as np


U=[Utterance.Utterance('some', ['all', 'notall']), Utterance.Utterance('all', ['all'])]
W=[World.World('all', 0.5), World.World('notall', 0.5)]
rationality=3.4
cost=0

def run_experiment(u,w, depth, cost, rationality):
	#creates an Rsa instance to run experiment
	rsa = Rsa.Rsa(u, w, cost, rationality)
	#compute the recursion
	rsa.recurse(depth, 0)
	#print out your final results
	for element in rsa.layers[depth].listener.table.possible_worlds:
		print "The utterance is " + str(element.utterance.u)
		print "The world is " + str(element.world.world)
		print "The column number is " + str(element.column)
		print "The row number is " + str(element.row)
		print "The probability is " + str(element.probability)
		print "--------------------"


#uncomment this if you want to run an experiment
run_experiment(U, W, 2, 0, 3.4)


#organizes the different experiments so that they can be easily graphed
def output(possible_worlds):
	results={}
	utterances=[]
	for world in possible_worlds:
		if world.utterance.u in results:
			results[world.utterance.u].append(world.probability)
		else:
		 results[world.utterance.u]=[world.probability]
		 utterances.append(world.utterance.u)
	return utterances, results

#graphs the model data and recurses through the model n times
def graph(experiment, n):
	exp_rsa=experiment.model(experiment.table, experiment.cost, experiment.rationality, n)
	u,r=output(experiment.possible_worlds)
	for utterance in u:
		ind = np.arange(4)  # the x locations for the groups
		width = 0.35       # the width of the bars
		fig, ax = plt.subplots()
		rects1 = ax.bar(ind, r[utterance], width, color='r')
		ax.set_xticks(ind + width / 2)
		ax.set_xticklabels(('0', '1', '2', '3'))
		ax.set_ylabel('probability')
		ax.set_title(utterance)
		ax.set_ylim([0,1])
	plt.show()
