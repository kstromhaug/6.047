import numpy
import pandas
import random

N = [0.1, 0.35, 0.25, 0.2, 0.1]
C = [0.05, 0.15, 0.2, 0.3, 0.3]
m = {0:0, 1:1, 2:2, 3:3, 6:4}
a = [0,1,2,3,6]


# Nsamples = []
# Csamples = []
# for i in range(10000):
# 	Nsamp = numpy.random.choice(a, 10, True, N)
# 	Nsamples.append(Nsamp)

# 	Csamp = numpy.random.choice(a, 10, True, C)
# 	Csamples.append(Csamp)


# Ns = pandas.DataFrame(Nsamples)
# Cs = pandas.DataFrame(Csamples)

# ClargerN = 0
# NlargerC = 0
# for i in range(len(Nsamples)):
# 	givenC = 1
# 	givenN = 1
# 	N_given_C
# 	for j in range(len(Nsamples[i])):
# 		NgivenC = givenC*C[m[Nsamples[i][j]]]
# 		NgivenN = givenN*N[m[Nsamples[i][j]]]
# 		N_given_C.append(C[])

# 		CgivenC = givenC*C[m[Csamples[i][j]]]
# 		CgivenN = givenN*N[m[Csamples[i][j]]]
# 	if NgivenC > NgivenN:
# 		ClargerN += 1
# 	if CgivenN > CgivenC:
# 		NlargerC += 1


# print ClargerN
# print NlargerC


Nseqs = []
Cseqs = []

partB = 0
partC = 0
for i in range(10000):
	Nseq = []
	Nscore = 1
	Cscore = 1
	for j in range(10):
		val = random.random()
# For N distribution
		if val < 0.1:
			Nseq.append(0)
			Nscore = Nscore * N[0]
			Cscore = Cscore * C[0]
			pass
		elif val < 0.45:
			Nseq.append(1)
			Nscore = Nscore * N[1]
			Cscore = Cscore * C[1]
		elif val < 0.7:
			Nseq.append(2)
			Nscore = Nscore * N[2]
			Cscore = Cscore * C[2]
		elif val < 0.9:
			Nseq.append(3)
			Nscore = Nscore * N[3]
			Cscore = Cscore * C[3]
		else:
			Nseq.append(6)
			Nscore = Nscore * N[4]
			Cscore = Cscore * C[4]
	Nseqs.append(Nseq)
	if Cscore > Nscore:
		partB = partB + 1

	Cseq = []
	Nscore = 1
	Cscore = 1
	for j in range(10):
		val = random.random()
# For N distribution
		if val < 0.05:
			Cseq.append(0)
			Nscore = Nscore * N[0]
			Cscore = Cscore * C[0]
			pass
		elif val < 0.2:
			Cseq.append(1)
			Nscore = Nscore * N[1]
			Cscore = Cscore * C[1]
		elif val < 0.4:
			Cseq.append(2)
			Nscore = Nscore * N[2]
			Cscore = Cscore * C[2]
		elif val < 0.7:
			Cseq.append(3)
			Nscore = Nscore * N[3]
			Cscore = Cscore * C[3]
		else:
			Cseq.append(6)
			Nscore = Nscore * N[4]
			Cscore = Cscore * C[4]
	Cseqs.append(Cseq)
	if Nscore > Cscore:
		partC = partC + 1

print partB
print partC

