import Rsa
import Speaker
class Listener:
	def __init__(self, speaker):
		self.speaker=speaker
		self.table=self.pragamtic_listener(speaker)

	def pragamtic_listener(self, speaker):
		print speaker.possible_worlds[0].probability
		self.table=speaker
		for world in self.table.possible_worlds:
			world.probability=world.probability*world.world.prior
		self.table.normalize(0)
		return self.table