def time_fn(ori_fn):
	def new_fn(*args, **kwargs):
		import datetime
		start = datetime.datetime.now()
		x = ori_fn(*args, **kwargs)
		end = datetime.datetime.now()
		print("Elapsed Time = {0}".format(end - start))
		return x
	return new_fn
# pie price matrix
# rows from top to bottom: john's shop, bob's shop, yue's shop
# cols from left to right: apple pie, cherry pie, blueberry pie, pumpkin pie
pie_price_matrix = [ 
	[  3, 4,   6,   6],
	[  4, 3,   5,   6],
	[3.5, 3, 6.5, 4.5],
]

# last week sale matrix assuming they all sell the same, silly but bear with me
# rows from top to bottom: apple pie, cherry pie, blueberry pie, pumpkin pie
# cols from left to right: Monday, Tuesday, Wesnesday, Thursday, Friday, Saturday, Sunday
last_week_sale_matrix = [
	[ 15, 18, 20, 10,  8, 25, 21 ],
	[ 14, 12, 10,  7, 16, 13, 11 ],
	[  7,  5, 17,  3,  9, 19, 13 ],
	[ 11, 14, 12,  8, 13, 10, 16 ]
]

class MatrixMultiply():
	def __init__(self, m1, m2):
		self.m1 = m1
		self.m2 = m2
		self.row = len(self.m1)
		self.col = len(self.m2[0])
		self.res = [ [0]*self.col for _ in range(self.row)]

	def add(self, m1, m2):
		self.m1 = m1
		self.m2 = m2
	def reset(self):
		for i in range(self.row):
			for j in range(self.col):
				self.res[i][j] = 0

	@time_fn
	def single_thread(self):
		for i in range(self.row):
			for j in range(self.col):
				for k in range(len(self.m1[0])):
					self.res[i][j] += self.m1[i][k] * self.m2[k][j]
		return self.res

if __name__ == "__main__":
	calculator = MatrixMultiply(pie_price_matrix, last_week_sale_matrix)
	print(calculator.single_thread())