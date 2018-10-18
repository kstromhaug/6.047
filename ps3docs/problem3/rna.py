import numpy as np
import pandas as pd
import random

RNAseqs = []

#  [A, U, C, G]
# A
# U
# C
# G
accessDict = {'A':0, 'U':1, 'C':2, 'G':3}
scoringMatrix = [[0, -1, 0, 0],
				[-1, 0, 0, -1],
				[0, -1, 0, -1],
				[0, -1, -1, 0]]

# first index is y, second index is x
def nussinov(rna):
	#initialization
	N = len(rna)
	y = [[None for i in range(N)] for i in range(N)]
	for l in range(N):
		y[l][l] = 0
	for l in range(1, N):
		y[l][l-1] = 0
	print y

	# propagatation
	for j in range(1, N):
		for i in range(0, N-i):
			#k = j + N - i
			nuc1 = rna[i]
			nuc2 = rna[j]
			print "hi"
			print i, j
			print y[i][j-1]
			y[i][j] = max(y[i+1][j], 
						y[i][j-1], 
						y[i+1][j-1] + scoringMatrix[accessDict[nuc1]][accessDict[nuc2]], # need to figure out what sigma is
						max(y[i][k]+y[k+1][j] for k in range(i+1,j)))
	return y

#def traceback(y):



# generate 1000 RNA sequences randomly

for i in range(1):
	RNA = []
	for j in range(10):
		val = random.random()
		if val < 0.25:
			RNA.append('A')
		elif val < 0.50:
			RNA.append('U')
		elif val < 0.75:
			RNA.append('C')
		else: RNA.append('G')
	rna = ''.join(RNA)
	RNAseqs.append(rna)

y = nussinov(RNAseqs[0])