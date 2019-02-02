class DllNode():
	def __init__(self, key, val):
		self.key = key
		self.val = val
		self.pre = None
		self.next = None

	def connect(self, node):
		self.next = node
		node.pre = self