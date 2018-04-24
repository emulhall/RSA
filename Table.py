import itertools
import Utterance
import PossibleWorld
#this table contains all the possible worlds
class Table:
	def __init__(self, possible_worlds, U, W):
		self.size=len(possible_worlds)
		self.possible_worlds=possible_worlds
		self.column_sums=[0]*self.size
		self.row_sums=[0]*self.size
		self.utterances=U
		self.worlds=W
		self.fill_sums(possible_worlds)

	#this adds up all of the possible world probabilities in the rows and columns of a table
	def fill_sums(self, possible_worlds):
		for world in possible_worlds:
			row=world.row
			column=world.column
			self.column_sums[column]+=world.probability
			self.row_sums[row]+=world.probability


	#re-adds up all of the columns and rows so that normalization is accurate
	def re_sum(self):
		self.column_sums=[0]*self.size
		self.row_sums=[0]*self.size
		self.fill_sums(self.possible_worlds)


	#important function for normalizing so that we can look at probability distributions
	def normalize(self, column):
		self.re_sum()
		for world in self.possible_worlds:
			if column:
				n=world.column 
				if world.probability==0 or self.column_sums[n]==0:
					pass
				else:
					world.probability=(world.probability)/(self.column_sums[n])
			else:
				n=world.row 
				if world.probability==0 or self.row_sums[n]==0:
					pass
				else:
					world.probability=(world.probability)/(self.row_sums[n])

	def copy(self):
		output=Table(self.possible_worlds, self.utterances, self.worlds)
		return output
