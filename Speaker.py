import Rsa
import Listener
import InitialListener
import math

class Speaker:
	def __init__(self, cost, rationality, listener):
		self.cost=cost
		self.rationality=rationality
		self.prev_listener=listener
		self.table=self.pragmatic_speaker(self.prev_listener)

	def pragmatic_speaker(self, listener):
		self.table=listener.table
		for world in self.table.possible_worlds:
			if world.probability==0:
				pass
			else:
				world.probability=math.exp(self.rationality*(math.log(world.probability) - self.cost))
		self.table.normalize(1)
		return self.table