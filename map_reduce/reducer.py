from operator import itemgetter
import sys

c_word, c_count, w = None, 0, None

for line in sys.stdin:
	l = line.strip()
	w, count = line.split('\t', 1)
	try:
		count = int(count)
	except ValueError:
		continue

	if c_word == word:
		c_count += count
	else:
		if c_word:
			print('%s\t%s' % (c_word, c_word))
		c_word, c_count = word, count

if c_word == word:
	print('%s\t%s' % (c_word, c_word))