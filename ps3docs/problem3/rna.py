import numpy as np
import pandas as pd
import random

#  [A, U, C, G]
# A
# U
# C
# G
accessDict = {'A':0, 'C':1, 'G':2, 'U':3}
scoringMatrix = [[0, 0, 0, -1],
				[0, 0, -1, 0],
				[0, -1, 0, -1],
				[-1, 0, -1, 0]]

# first index is y, second index is x
def nussinov(rna, var):
	#initialization
	#print rna
	rna = rna[0]
	N = len(rna)
	y = np.zeros((N,N))
	# if var < 10:
	# 	print rna
	# 	print y

	# propagatation
	for m in range(1, N):
		for i in range(0, N-m):
			j = m+i

			a = []
			for k in range(j+1, i):
				a.append(y[i][k]+y[k+1][j])
			if a == []:
				a = [0]

			nuc1 = rna[i]
			nuc2 = rna[j]
			y[i][j] = min(y[i+1][j], 
						y[i][j-1], 
						y[i+1][j-1] + scoringMatrix[accessDict[nuc1]][accessDict[nuc2]], 
						min(a))
	# if var <= 10:
	# 	print y
	return y[0][N-1]




# generate 1000 RNA sequences randomly
def getseqs():
	RNAseqs = []
	for i in range(1000):
		RNA = []
		for j in range(100):
			val = random.random()
			if val < 0.25:
				RNA.append('A')
			elif val < 0.50:
				RNA.append('U')
			elif val < 0.75:
				RNA.append('C')
			else: RNA.append('G')
		#rna = ''.join(RNA)
		RNAseqs.append(RNA)
	return RNAseqs

#def main():

if __name__ == '__main__':
	seqs = getseqs()
	scores = np.zeros(1000, dtype=np.int)

	for i in range(len(seqs)):
		#if i < 10:
			#print seqs[i]
		nus = nussinov([seqs[i]], i)
		scores[i] = nus
	print scores
	print np.mean(scores)

#y = nussinov(['G', 'G', 'G', 'A', 'A', 'A', 'U', 'C', 'C'])


"""
PWM can just be background
calculate background matrix

have PWM
create Zij using all seqs - 1 random seq

Z is a probability distribution

do random.choice(range(sequence)Z[i]) 

start at that place for the squence. That where we think the sequence will start.

Update PWM usign that value

Make new Zij

exit if you converge. If the newPWM - prevPWM is small in all locations


"""