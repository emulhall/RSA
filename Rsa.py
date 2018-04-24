import Table
import Utterance
import PossibleWorld
import itertools
import math
import World
import Layer
import InitialListener
import Speaker
import Listener

class Rsa:
	def __init__(self, U, W, cost, rationality):
		self.utterances=U
		self.worlds=W
		self.initial_listener=InitialListener.InitialListener(U, W)
		self.cost=cost
		self.rationality=rationality
		self.layers=[]
		self.layers.append(Layer.Layer(self.initial_listener, None, 0))


	#this recurses through and computes the probabilities
	def recurse(self, depth, n):
		while(n<depth):
			speaker=Speaker.Speaker(self.cost, self.rationality, self.layers[n].listener)
			listener=Listener.Listener(speaker.table.copy())
			n+=1
			self.layers.append(Layer.Layer(listener, speaker, n))
		return self.layers

