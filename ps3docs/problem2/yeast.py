import numpy
import math
import pandas
import itertools

# calculate all kmers

k = 6

allkmers = [''.join(i) for i in itertools.product('ATCG', repeat = 6)]

#print allkmers

