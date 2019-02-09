from util.util_tree_like import Trie

def testTrie():
	t = Trie()
	t.insert('the')
	print(t.search('the'))
	print(t.search('t'))
	print(t.search('these'))
	t.insert('these')
	t.insert('their')
	t.displayAll()
def main():
	#testTrie()

main()