from util.util_graph_like import Matrix
import collections
class S1():
	def isValid(self,r,c,row,col):
		if 0 <= r < row and 0 <= c < col:
			return True
		return False
    
	def dfs(self,grid,r,c,visit,row,col):
		visit[r][c] = 1
		ad_r = [-1,0,0,1]
		ad_c = [0,-1,1,0]
        
		for k in range(0, len(ad_r)):
			n_r = r + ad_r[k]
			n_c = c + ad_c[k]
			if self.isValid(n_r,n_c,row,col) and visit[n_r][n_c] == 0 and grid[n_r][n_c] == '1':
				self.dfs(grid,n_r,n_c,visit,row,col)
    
	def numOfIslands(self, grid):
		if len(grid) == 0:
			return 0
		row = len(grid)
		col = len(grid[0])
		visit = []
		count = 0
		for i in range(0,row):
			new_col = [0]*col
			visit.append(new_col)

		for i in range(0,row):
			for j in range(0,col):
				if visit[i][j] == 0 and grid[i][j] == '1':
					self.dfs(grid,i,j,visit,row,col)
					count += 1
                    
		return count

def testNumberOfIsland():
	s1 = S1()
	config = {'row': 5, 'col': 7, 'is_directed': True}
	m_obj = Matrix(config)
	m = m_obj.randomMatrixWithZeroOne()
	print("Matrix:")
	print(m)
	res = s1.numberIslandsOne(m)
	print(res)

class S2():
	def __init__(self):
		self.g = {}
		self.res = []

	def buildGraph(self, word_list):
		self.g = {}
		self.res = []
		for i in range(len(word_list)-1):
			w1, w2 = word_list[i], word_list[i+1]
			for c in w1:
				self.g[c] = self.g.get(c,[])
			for i in range(min(len(w1), len(w2))):
				c1, c2 = w1[i], w2[i]
				if c1 != c2:
					if c2 not in self.g[c1]:
						self.g[c1].append(c2)
					break
	def dfs(self, node, visited, visiting):
		visited.add(node)
		visiting.add(node)
		for nei in self.g[node]:
			if nei not in visited:
				if self.dfs(nei, visited, visiting):
					return True
		visiting.remove(node)
		self.res.append(node)
		return False
	def alianDictionary(self, word_list):
		self.buildGraph(word_list)
		visited, visiting = set(), set()
		for node in self.g:
			if node not in visited:
				if self.dfs(node, visited, visiting):
					return -1
		self.res.reverse()
		return "".join(self.res)

def testAlianDictionary():
	solution = S2()
	input = ["wrt","wrf","er","ett","rftt"]
	res = solution.alianDictionary(input)
	print("Result:")
	print(res)

def testGraphGeneration():
	config = {'row': 6, 'col': 6, 'is_directed': False}
	m_obj = Matrix(config)
	m = m_obj.randomGraphInMatrix()
	print("Graph:")
	print(m)

def testSpiralMatrix():
	config = {'row': 6, 'col': 6, 'is_directed': False}
	m_obj = Matrix(config)
	m = m_obj.generateSpiralMatrix()
	print("SpiralMatrix:")
	print(m)

class S3():
	def buildStopToBus(self, b2s):
		g = {}
		for bus,stops in enumerate(b2s):
			for stop in stops:
				g[stop] = g.get(stop, []) + [bus]
		return g

	def busRoute(self, input):
		b2s, s, e = input['b2s'], input['start'], input['end']
		s2b = self.buildStopToBus(b2s)
		visited_stop, visited_bus = set(), set()
		q, step = collections.deque(), 1
		q.append(s)
		while q:
			n = len(q)
			for i in range(n):
				current = q.popleft()
				if current == e:
					return step
				visited_stop.add(current)
				for bus in s2b[current]:
					if bus not in visited_bus:
						for stop in b2s[bus]:
							if stop not in visited_bus:
								if stop == e:
									return step
								q.append(stop)
			step += 1

		return step

def testBusRoute():
	input = {
		'b2s':[
			[1, 2, 7, 10, 15, 23],
			[3, 6, 7, 14, 16, 21],
			[4, 5, 8, 17, 18, 23, 35],
			[1, 6, 9, 11, 17, 19, 22],
			[2, 3, 4, 5, 7, 20, 24, 26, 28]
		],
		'start': 1,
		'end': 35
	}

	s3 = S3()
	res = s3.busRoute(input)
	print(res)

class S4():
	def minMalwareSpread(self, graph, initial):
		def dfs(node, visited):
			visited.add(node)
			for i in range(len(graph)):
				if i != node and i not in visited and graph[node][i]:
					dfs(i, visited)

		if len(initial) == 0:
			return None
		res = initial[0]
		mini = -1
		while initial:
			c_node = initial[0]
			visited, old = set(), set(initial)
			dfs(c_node, visited)

			interset = visited & old
			if len(interset) == 1:
				num_of_nodes = len(visited)
				if num_of_nodes > mini:
					res = c_node
					mini = num_of_nodes
				elif num_of_modes == mini:
					res = min(res, c_node)
			else:
				if mini <= 0:
					mini = 0
					res = min(res, sorted(interset)[0])
			new = old - interset
			initial = list(new)
		return res      
	
def testMalware():
	s = S4()
	config = {'row': 7, 'col': 7, 'is_directed': False}
	m_obj = Matrix(config)
	m = m_obj.randomGraphInMatrix()
	print(m)
	init = [6,0,1,2]
	print(s.minMalwareSpread(m, init))

class S5():
	def game_of_life(self, b):
		ad = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
		def checkNeighbors(i, j):
			count = 0
			for ad_i, ad_j in ad:
				n_i, n_j = i+ad_i, j+ad_j
				if 0 <= n_i < len(b) and 0 <= n_j < len(b[0]) and (b[n_i][n_j]%2) == 1:
					count += 1
			return count
		'''[
			[1,0,0],
			[0,1,0],
			[0,1,0]
		]'''
		for i in range(len(b)):
			for j in range(len(b[0])):
				count = checkNeighbors(i, j)
				if b[i][j] == 1:
					if count < 2 or count > 3:
						b[i][j] = 3
				elif b[i][j] == 0:
					if count == 3:
						b[i][j] = 2
		for i in range(len(b)):
			for j in range(len(b[0])):
				if b[i][j] == 3:
					b[i][j] = 0
				elif b[i][j] == 2:
					b[i][j] = 1
		return b

def test_game_of_life():
	s = S5()
	m_obj = Matrix()
	m = m_obj.randomMatrixWithZeroOne()
	print('Before:')
	print(m)
	print('After:')
	print(s.game_of_life(m))


def main():
	#testNumberOfIsland()
	#testGraphGeneration()
	#testAlianDictionary()
	#testSpiralMatrix()
	#testBusRoute()
	#testMalware()
	#test_game_of_life()
main()