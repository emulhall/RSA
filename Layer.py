
class Layer:
	def __init__(self, n):
		self.n=n

	def __init__(self, listener, speaker, n):
		self.n=n
		self.listener=listener
		self.speaker=speaker

	def set_listener(self, listener):
		self.listener=listener

	def get_listener(self):
		return self.listener

	def set_speaker(self, speaker):
		self.speaker=speaker

	def get_speaker(self):
		return self.speaker

