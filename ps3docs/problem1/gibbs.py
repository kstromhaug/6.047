#!/usr/bin/env python
import sys
import string
import random
import math
import numpy

#### INSTRUCTIONS FOR USE:
# call program as follows: ./gibbs.py <Motif Length> <Data File>
# make sure the gibbs.py is marked as executable: chmod +x gibbs.py

alphabet = ['A', 'G', 'C', 'T']
ad = {'A':0, 'G':1, 'C':2, 'T':3}

#### GibbsSampler:
#### 	INPUTS:	S - list of sequences
####		L - length of motif
####	OUTPUT:	PWM - 4xL list with frequencies of each base at each position
####                  Order of bases should be consistent with alphabet variable
def GibbsSampler(S,L):

    PWM = numpy.ones((len(alphabet), L))

    ######### ADD YOUR CODE HERE ######

    # How do I decide which sequence to skip?

    nSeqs = len(S)
    startInts = []

    # calculating the random start points for the first iteration
    for i in range(nSeqs):
        start = random.randint(0,len(S[i])-L) #the start for this 
        startInts.append(start)
    print startInts, 0
    # deciding which one to skip
    skip = random.randint(0, nSeqs)

    # counting up the number of nucleotides of each identity at each position
    PWM = pwmCount(skip, PWM, S, L, startInts)

    # calculating the log probabilities from the counts above
    PWMprobs = PWM/float(nSeqs-1+4)
    PWMprobs = numpy.log(PWMprobs)

    # calculating the probabilities at starting at each position given the current PWM
    allprobs = probDistributions(S, PWMprobs, L, nSeqs)

    oldPWM = PWMprobs
    # go until convergence
    go = True
    while go == True:

        #oldPWM = PWMprobs

        # use this distribution to calculate the next starting point based on that distribution
        newStartPoints = []
        for i in range(nSeqs):
            dist = numpy.array(allprobs[i])
            normdist = numpy.power(math.e, dist)
            probsum = numpy.sum(normdist)
            normdist = normdist / probsum
            startpoint = numpy.random.choice(range(len(S[i])-L+1), 1, True, normdist)
            newStartPoints.append(startpoint[0])
        #print newStartPoints
        # new row to skip
        skip = random.randint(0, nSeqs)

        # new PWM
        PWM = numpy.ones((len(alphabet),L))
        PWM = pwmCount(skip, PWM, S, L, newStartPoints)

        # new PWM log probs
        PWMprobs = numpy.divide(PWM, float(nSeqs-1+4))
        PWMprobs = numpy.log(PWMprobs)

        # check the differece between old and new
        diffs = abs(numpy.subtract(PWMprobs, oldPWM))
        if diffs.any() > 0.5:
            go = True
            allprobs = probDistributions(S, PWMprobs, L, nSeqs)
            oldPWM = PWMprobs

        else:
            go = False

    seqs_for_fasta = []
    for i in range(len(S)):
        start = newStartPoints[i]
        seqs_for_fasta.append(S[i][start:start+L])

    with open('fasta2.fa', 'w') as f:
        for seq in seqs_for_fasta:
            f.write('>\n')
            f.write(seq)
            f.write('\n')
    f.close()
    ######### END OF YOUR CODE HERE #####
	
    return PWM

###### YOUR OWN FUNCTIONS HERE
# optional -- feel free to add your own functions if you want to
def pwmCount(skip, PWM, S, L, startInts):
    # counting up the number of nucleotides of each identity at each position
    for i in range(skip) + range(skip+1, len(S)):    #iterating through sequences
        for j in range(L):  #
            index = startInts[i]+j
            nuc = S[i][index]
            PWM[ad[nuc]][j] += 1
    return PWM

def probDistributions(S, PWMprobs, L, nSeqs):

        # calculating the probabilities at starting at each position given the current PWM
        # for one seq, make this a loop for them all later
        # use rolling hashing

    allprobs = []
    for seq in S:
        sProbs = []
        for j in range(len(seq)-L+1):
            prob = 0
            for k in range(L):
                index = j+k
                nuc = seq[index]
                prob += PWMprobs[ad[nuc]][k] # changed from +=
            sProbs.append(prob)
        allprobs.append(sProbs)
    return allprobs



    # allprobs = []
    # for i in range(nSeqs):
    #     sProbs = []
    #     prob = 0
    #     for j in range(L):
    #         nuc = S[i][j]
    #         prob += PWMprobs[ad[nuc]][j]
    #     sProbs.append(prob)

    #     for j in range(L, len(S[i])):
    #         remnuc = S[i][j-L]
    #         prob -= PWMprobs[ad[remnuc]][0]   #subtract the first probability
    #         prob += PWMprobs[ad[nuc]][L-1]      #add the current probability
    #         sProbs.append(prob)
    #     allprobs.append(sProbs)
    # return allprobs
###### END OF YOUR FUNCTIONS

def main():
    L = int(sys.argv[1])
    datafile = sys.argv[2]
    S = readdata(datafile)
	
    P = GibbsSampler(S,L)
	
    print "    ", 
    for i in range(L):
        print "%-5d " % (i+1),
    print ""
	
    for j in range(len(alphabet)):
        print " %s " % alphabet[j], 
        for i in range(L):
            print " %5.3f" % P[j][i],
        print ""

    motif = []
    for i in range(L):
        maxnuc = 0
        ind = 0
        for j in range(4):
            #print P[j][i]
            if P[j][i] > maxnuc:
                maxnuc = P[j][i]
                ind = j
        motif.append(alphabet[ind])
    motif = ''.join(motif)
    print motif
    for seq in S:
        if motif in seq:
            print True
        else:
            print False

	
def readdata(file):
    data = [];
    for line in open(file,'r'):
        data.append(line[0:-1])
    return data

main()

