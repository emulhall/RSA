import Rsa
import Table
import itertools
import PossibleWorld
class InitialListener:
	def __init__(self, U, W):
		self.utterances=U
		self.worlds=W
		self.possible_worlds=self.make_worlds(U, W, 0, -1, [])
		self.table=Table.Table(self.possible_worlds, U, W)
		self.table.normalize(0)

	#iterates through the list of utterances and the list of worlds in order to make all possible worlds
	def make_worlds (self, U, W, x, y, worlds):
		row=list(itertools.product([U[0]], W))
		for pair in row:
			y+=1
			worlds.append(PossibleWorld.PossibleWorld(pair[0], pair[1], x, y))
		if len(U)==1:
			return worlds
		else:
			return self.make_worlds(U[1:], W, x+1,-1, worlds)