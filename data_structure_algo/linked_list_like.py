from util.util_linked_list_like import DllNode

class LRUCache():
	def __init__(self, cap):
		self.head = DllNode(None, None)
		self.tail = DllNode(None, None)
		self.head.connect(self.tail)
		self.map = {}
		self.cap = cap
		self.size = 0

	def __add(self, node):
		node.connect(self.head.next)
		self.head.connect(node)
		self.map[node.key] = node

	def __remove(self, node):
		self.map.pop(node.key)
		node.pre.connect(node.next)

	def get(self, key):
		if key not in self.map:
			return False
		node = self.map[key]
		self.__remove(node)
		self.__add(node)
		return node.val

	def set(self, key, val):
		if key in self.map:
			node = self.map[key]
			node.val = val
			self.__remove(node)
			self.__add(node)
		else:
			if self.size >= self.cap:
				last = self.tail.pre
				self.__remove(last)
			else:
				self.size += 1
			node = DllNode(key, val)
			self.__add(node)
		return

	def display(self):
		tmp = self.head.next
		res = []
		while tmp != self.tail:
			res.append((tmp.key,tmp.val))
			tmp = tmp.next
		print(res)

def testLRUCache():
	cache = LRUCache(5)
	print(cache.get(1))
	cache.set(1,10)
	cache.set(2,20)
	cache.set(3,30)
	cache.set(4,40)
	cache.set(5,50)
	cache.get(1)
	cache.get(2)
	cache.display()
	cache.set(6,60)
	cache.set(4,400)
	cache.display()

def main():
	testLRUCache()

main()