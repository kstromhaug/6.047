import numpy
import math
import pandas
import itertools
import sys

# calculate all kmers

k = 6

allkmers = [''.join(i) for i in itertools.product('ATCG', repeat = 6)]

#print allkmers


def readdata(file):
    data = [];
    for line in open(file,'r'):
        data.append(line[0:-1])
    return data

if __name__ == '__main__':
    datafile = sys.argv[1]
    consfile = sys.argv[2]
    S = readdata(datafile)
    S = S[0]
    C = readdata(consfile)
    C = C[0]
    print len(C) == len(S)
    compareDict = {}
    for i in range(len(S)-k):
    	if S[i] == '-':
    		pass
    	elif S[i:i+k] not in compareDict:
    		if C[i:i+k] == '******':
	    		compareDict[S[i:i+k]] = [1,1]
	    	else:
	    		compareDict[S[i:i+k]] = [1,0]
    	else:
    		compareDict[S[i:i+k]][0] += 1
    		if C[i:i+k] == '******':
	    		compareDict[S[i:i+k]][1] += 1

    kCounts = {}
    for kmer in allkmers:
    	if kmer not in compareDict:
    		kCounts[kmer] = [0,0]
    	else:
    		kCounts[kmer] = [compareDict[kmer][0], compareDict[kmer][1]/float(compareDict[kmer][0])]

    kCountsDF = pandas.DataFrame.from_dict(kCounts, orient='index')
    sortedDF = kCountsDF.sort_values(0, ascending=False)
    fiddyfreq = sortedDF[:50].index
    sortedDF2 = kCountsDF.sort_values(1, ascending=False)
    fiddycont = sortedDF2[:50].index

    with open('most_freq.txt', 'w') as f:
    	for seq in fiddyfreq:
	    	f.write(seq)
	    	f.write('\n')
    f.close()

    with open('most_cons.txt', 'w') as f:
    	for seq in fiddycont:
	    	f.write(seq)
	    	f.write('\n')
    f.close()


    with open('yeast_motifs.txt', 'r') as f:
    	data = []
    	for line in f:
    		data.append(line)
    f.close()
    #print data

    for seq in fiddycont:
    	for mot in data:
    		start = mot.find(' ')+1
    		#print seq, mot[start:-1]
    		if seq == mot[start:-1]:
    			print seq, mot
    #print kCounts

   #  kmerCounts = []
   #  for kmer in allkmers[0:50]:
   #  	kcount = 0
   #  	for i in range(len(S)):
			# if S[i] == '-':
			# 	continue
			# elif 

    	#kmerCounts.append(kcount)
    #print kmerCounts[0:50]

