import random
class Matrix():
	def __init__(self, setting):
		self.default = ['row', 'col', 'is_directed']
		self.config = { 'row': 5, 'col': 5, 'is_directed': True }
		if setting:
			self.updateMatrixSetting(setting)

	def __displayConfig(self):
		print(self.config)

	def __initialMatrix(self):
		m = [ [0]*self.config['col'] for _ in range(self.config['row']) ]
		return m

	def updateMatrixSetting(self, setting):
		for key in self.default:
			if key in setting:
				self.config[key] = setting[key]

	def __updateSpecificRow(self, m, r, start_c):
		c = self.config['col']
		l = c-start_c
		seed = random.randint(0,2**l-1)
		for j in range(start_c, c):
			num = (seed>>(l-1)) & 1
			m[r][j] = num
			l -= 1
			if self.config['is_directed'] == False and j != start_c:
				m[j][r] = num


	def randomMatrixWithZeroOne(self):
		m = self.__initialMatrix()
		for i in range(self.config['row']):
			self.__updateSpecificRow(m,i,0)
		print('Current Config:')
		self.__displayConfig()
		return m

	def randomGraphInMatrix(self):
		m = self.__initialMatrix()
		for i in range(self.config['row']):
			if self.config['is_directed']:
				self.__updateSpecificRow(m,i,0)
			else:
				self.__updateSpecificRow(m,i,i)
		for i in range(self.config['row']):
			m[i][i] = 1
		print('Current Config:')
		self.__displayConfig()
		return m

	def generateSpiralMatrix(self):
		m = self.__initialMatrix()
		n, maxi = 1, self.config['row'] * self.config['col']
		t, l = 0, 0
		b, r = self.config['row']-1, self.config['col']-1
		i, j = 0,0
		while t < b or l < r:
			while j < r+1:
				m[t][j] = n
				n += 1
				j += 1
			t += 1
			i = t
			while i < b+1:
				m[i][r] = n
				n += 1
				i += 1
			r -= 1
			j = r
			while j > l-1:
				m[b][j] = n
				n += 1
				j -= 1
			b -= 1
			i = b
			while i > t-1:
				m[i][l] = n
				n += 1
				i -= 1
			l += 1
			j = l
		return m
