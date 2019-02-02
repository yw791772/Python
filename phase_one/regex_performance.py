import regex
import time
import sys
import getopt

def testRegex(loop):
	with open('test.txt', 'r') as content_file:
		content = content_file.read()

	t1, t2 = 0, 0

	for _ in range(loop):
		s1 = time.time()
		result = regex.search("meta", content)
		e1 = time.time()
		t1 += s1-e1

		s2 = time.time()
		result = regex.search("[a-z]{5}\.[a-z]{1}", content)
		e2 = time.time()
		t2 += s2-e2

	avg1 = t1/loop*1000
	avg2 = t2/loop*1000

	print("First expression average in milliseconds: ", avg1)
	print("Second expression average in milliseconds: ", avg2)

	print("First one is faster") if avg1 > avg2 else print("Second one is faster")

try:
	opts, args = getopt.getopt(sys.argv[1:], "", ["help=", "loop="])
except getopt.GetoptError:
	print('regex_performance.py --loop 2000')
	sys.exit(2)
for opt, arg in opts:
	if opt == '--help':
		print('regex_performance.py --loop 2000')
		sys.exit()
	elif opt == '--loop':
		loop = arg
		if not loop.isdigit():
			print('regex_performance.py --loop 2000')
		else:
			testRegex(int(loop))