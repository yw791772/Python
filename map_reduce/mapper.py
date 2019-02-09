import sys

for line in sys.stdin:
	l = line.strip()
	words = line.split()
	for w in words:
		print("%s\t%s" % (w, 1))