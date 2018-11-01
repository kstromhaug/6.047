import math
import numpy
import pandas
import random
import scipy.stats
#################

# DO THE IMORTING OF VALUES FROM TERMINAL

##################	

"""
k = number of disease-related snps
n = number of people
m = number snps (each occur in population with prob 0.05)
s = standard deviation for normal distribution of beta values pertaining
	each of the k snps
	- one s pertains to all of the disease-related snps
"""

n = 10000
k = 100
m = 10000
s = 0.25

def gen_sequences(n, k, m, s):
	#snpData = pandas.DataFrame(index = range(n), columns = ['sequence', 'epsilon'])
	
	# randomly choose which k snps are disease causing
	disease_snps = []
	for x in range(k):
		disease_snps.append(random.randint(0, m))

	# give disease causing snps beta's from appropriate s
	# give other snps a beta of 0
	betas = []
	for i in range(m):
		if i in disease_snps:
			betas.append(numpy.random.normal(loc = 0.0, scale = s))
		else:
			betas.append(0) # because non-disease snps shouldn't affect the equation

	# randomly generate the genes, sequences of 0s and 1s
	# randodmly generate epsilons from distribution given
	genes = []
	epsils = []
	for k in range(n):
		gene = []
		for i in range(m):
			num = numpy.random.random()
			if num < 0.95:
				gene.append(0)
			else:
				gene.append(1)
		eps = numpy.random.normal(loc=0.0, scale=1)
		epsils.append(eps)
		genes.append(gene)
		#snpData.set_value(k, 'sequence', gene)
		#snpData.set_value(k, 'epsilon', eps)

	has_disease = []

	inv_genes = numpy.array(genes).T
	ys = numpy.dot(betas, inv_genes) + epsils


	genes = numpy.array(genes)
	num_ones = genes.sum(axis=0)	# sum of each columns 
	snp_ones = genes.sum(axis=1)	# the number of 1s in each person
	total = num_ones.sum()
	expected_ones = total/(m*n)
	num_zeroes = n-num_ones
	contingency = numpy.concatenate(([num_ones],[num_zeroes]), axis=0)
	#print contingency

	chi_square, p, dof, ex = scipy.stats.chi2_contingency(contingency, correction=False)
	print chi_square
	print p
	print dof
	print ex

	new_p = float(p)/(2*m)
	print new_p



	#print has_disease

	# chi-square test of all snps
	# null hypothesis: snp is not disease causing
	# assuming null hypothesis,
	# calculate probability.....
	# need sum of 0s, sum of 1s, and total sum
	# calculate the percentage of  0's and 1's
	# - Sum across rows, to get number of snps
	# - caluclate percentages
	# - predict what the frequency of that snp should be
	for i in range(m):
		pass

	return 0


gen_sequences(n, k, m, s)