#combines an utterance with a world
class PossibleWorld:
	def __init__(self, U, W, row, column):
		self.utterance=U
		self.world=W
		self.column=column
		self.row=row
		self.probability=self.l0(U, W)

#this is essentially the intial listener - it compares w to all of the possible meanings for the utterance and w is a meaning
#if the world and the set of meanings an utterance produces overlaps, then it returns the prior (and otherwise returns 0)
#essentially, this function combines the lexicon and l0 steps
	def l0(self, U, W):
		if W.world in U.meaning:
			return W.prior
		else:
			return 0