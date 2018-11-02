import math
import numpy
import pandas
import random
import scipy.stats
from scipy import stats
#from scipy.stats import chisqprob
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
m = 1000
s = 0.25

def gen_sequences(n, k, m, s):
	#snpData = pandas.DataFrame(index = range(n), columns = ['sequence', 'epsilon'])
	
	# randomly choose which k snps are disease causing
	disease_snps = []
	for x in range(k):
		disease_snps.append(random.randint(0, m))
	print disease_snps

	# give disease causing snps beta's from appropriate s
	# give other snps a beta of 0
	betas = []
	kSNPs = []
	for i in range(m):
		if i in disease_snps:
			betas.append(numpy.random.normal(loc = 0.0, scale = s))
			kSNPs.append(True)
		else:
			betas.append(0) # because non-disease snps shouldn't affect the equation
			kSNPs.append(False)

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
	healthy_ppl = []
	inv_genes = numpy.array(genes).T
	ys = numpy.dot(betas, inv_genes) + epsils

	for i in range(n):
		if ys[i] > 2:
			has_disease.append(i)
		else:
			healthy_ppl.append(i)
	print len(has_disease)

	genes = numpy.array(genes)

	diseased = genes[has_disease,:]		#subset determined to have the disease
	healthy = genes[healthy_ppl,:]		#subset determined to to be healthy


	print len(diseased), len(healthy), len(genes)

	diseased_with_one = diseased.sum(axis=0)
	healthy_with_one = healthy.sum(axis=0)

	chi_squares = []
	ps = []
	dofs = []
	exs = []
	for i in range(m):
		square = [[0,0], [0,0]]
		square[0][0] = diseased_with_one[i]
		square[0][1] = healthy_with_one[i]
		square[1][0] = len(diseased)-diseased_with_one[i]
		square[1][1] = len(healthy)-healthy_with_one[i]
		if i < 10:
			print square
		chi_square, p, dof, ex = scipy.stats.chi2_contingency(square, correction=False)

		chi_squares.append(chi_square)
		ps.append(p)
		dofs.append(dof)
		exs.append(ex)

	#print scipy.stats.chi2_contingency([[30, 90],[40, 100]], correction=False)

	print chi_squares[:10]
	print ps[:10]


	###########*********##########*********
	# HOW DO I DETERMINE IF I PREDICTED THE SNP TO BE BENIGN OR DISEASE CAUSING?
	# ONLY MISSING PIECE NOW
	###########*********##########*********

	# ACCURACY
	# (TP+TN)/(TP+TN+FP+FN)

	predicted_disease_snps = []
	for i in range(m):
		# add True if predicted to be a SNP and False if not
		pass


	confusion = [[0,0],[0,0]]
	for i in range(m):
		if predicted_disease_snps[i] == False and kSNPs[i] == False:
			confusion[0][0] += 1
		elif predicted_disease_snps[i] == True and kSNPs[i] == False:
			confusion[0][1] += 1
		elif predicted_disease_snps[i] == False and kSNPs[i] == True:
			confusion[1][0] += 1
		else:
			confusion[1][1] += 1

	accuracy = float((confusion[0][0]+confusion[1][1])) / (sum(confusion[0])+sum(confusion[1]))

	# PRECISION
	# TP / predicted yes
	precision = confusion[1][1]/(confusion[0][1]+confusion[1][1])

	print accuracy, precision
	return 0

gen_sequences(n, k, m, s)
