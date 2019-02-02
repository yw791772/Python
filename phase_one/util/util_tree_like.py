class TrieNode():
	def __init__(self, label):
		self.label = label
		self.children = {}
		self.is_end = False

class Trie():
	def __init__(self):
		self.root = TrieNode(None)

	def insert(self, word):
		tmp = self.root
		for c in word:
			if c not in tmp.children:
				nn = TrieNode(c)
				tmp.children[c] = nn
			tmp = tmp.children[c]
		tmp.is_end = True

	def search(self, word):
		tmp = self.root
		for c in word:
			if c not in tmp.children:
				return False
			tmp = tmp.children[c]
		if not tmp.is_end:
			return False
		return True

	def displayAll(self):
		res = []
		def dfs(node, current):
			if node.is_end:
				res.append(current+node.label)
			for key in sorted(node.children):
				dfs(node.children[key], current+node.label)

		for key in sorted(self.root.children):
			dfs(self.root.children[key], '')
		print(res)