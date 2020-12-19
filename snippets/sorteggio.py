import random
import sys

def sorteggio(max):
	r = [x for x in range(max)]
	random.shuffle(r)
	for i in r:
		print(i, end=" ")


sorteggio(int(sys.argv[1]))
