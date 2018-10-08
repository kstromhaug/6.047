import sys
from math import *
from subprocess import call
from numpy import *
import random


def assignPoints(tbl, ctrs):
    """Assign each of the points in tbl to the cluster with
        center in ctrs"""

    ptsAsgn = [];

    """SOME CODE GOES HERE"""
    """make sure that your code returns a vector
        that codes the cluster assignments as 0,1,and 2"""

    for point in tbl:
        distsum = 0
        ctrArray = [0] * len(ctrs)
        for i in range(len(ctrs)):
    	    dist = euclideanDist(point, ctrs[i])
            ctrArray[i] = dist
            distsum += dist
        for i in range(len(ctrs)):
            ctrArray[i] = ctrArray[i]/distsum

        ptsAsgn.append(ctrArray)


    return ptsAsgn


def recalculateCtrs(tbl, ctrs, ptsAsgn):
    """Update the centroids based on the points assigned to them"""

    xy = [[0,0]] * len(ctrs)

    """SOME CODE GOES HERE"""

    for j in range(len(ctrs)):
        probsum = 0
        for i in range(len(tbl)):
            xy[j][0] += tbl[i][0]*ptsAsgn[i][j]
            xy[j][1] += tbl[i][1]*ptsAsgn[i][j]
            probsum += ptsAsgn[i][j]

        for k in range(len(xy)):
            xy[k][0] = xy[k][0]/probsum
            xy[k][1] = xy[k][1]/probsum

    return xy


def euclideanDist(x, y):

    if len(x) != len(y):
        print "x and y must be the same length"
        sys.exit(1)
    else:
        dist_val = 0
        for i in xrange(len(x)):
            dist_val = dist_val + math.pow((x[i] - y[i]),2)

    return math.sqrt(dist_val)


def plotClusters(tbl, ptMemb, cntrs, stepCnt, anLabel):
    """generate a scatterplot of the current
       k-means cluster assignments

       filename may end in the following file extensions:
         *.ps, *.png, *.jpg
    """

    p = open("./" + anLabel + "_output/dummy_table.txt", "w")

    for i in xrange(len(tbl)):
        for j in xrange(len(tbl[i])):
            p.write(`tbl[i][j]`)
            p.write("\t")
        p.write(`ptMemb[i]`)
        p.write("\n")

    for i in xrange(len(cntrs)):
        for j in xrange(len(cntrs[i])):
            p.write(`cntrs[i][j]`);
            p.write("\t")
        p.write("Clust" + `i`)
        p.write("\n")

    p.close()

    plotCMD = "R CMD BATCH '--args ./" + anLabel + "_output/dummy_table.txt ./" + anLabel + "_plots/cluster_step%d.png" % stepCnt + "' ./kmeans_plot.R;"
    call(plotCMD, shell=True)



###############################################################################
# MAIN
###############################################################################

def main():

    """Checks if we have the right number of command line arguments
       and reads them in"""
    if len(sys.argv) < 1:
        print "you must call program as: python ./kmeans.py <datafile>"
        sys.exit(1)
    analysis_name = sys.argv[1]

    """creates directories for storing plots and intermediate files"""
    # call(["rm", "-r", "./" + analysis_name + "fuzzy_plots/"])
    # call(["mkdir", "-p", "./" + analysis_name + "fuzzy_plots/"])
    # call(["mkdir", "-p", "./" + analysis_name + "fuzzy_output/"])

    """Reads in the point data from the given tissue file"""
    dataTable = [];
    f = open("./" + analysis_name + "_data.txt")
    for dataLine in f:
        dataTable.append([float(str) for str in dataLine.rstrip().split("\t")])
    f.close()

    """initializes centroids, stop criterion and step counting for clustering"""
    newCtrs = [[5,0], [5,40], [5,80]]
 #    r = []
 #    for x in range(6):
	# r.append(random.randint(1,101))
 #    newCtrs = [[r[0],r[1]], [r[2],r[3]], [r[4],r[5]]]

    ptMemb = assignPoints(dataTable, newCtrs)
    stopCrit = False
    stepCount = 1

    """performs k-means clustering, plotting the clusters at each step"""
    while stopCrit == False:
        plotClusters(dataTable, ptMemb, newCtrs, stepCount, analysis_name)

        """SOME CODE GOES HERE"""
	oldCtrs = newCtrs
        newCtrs = recalculateCtrs(dataTable, oldCtrs, ptMemb)

        ptMemb = assignPoints(dataTable, newCtrs)

        """stop criterion - when centroids' total movement after a step is below
            the threshold, stop the algorithm"""
        stopDist = 0;
        for i in xrange(len(newCtrs)):
            stopDist = stopDist + euclideanDist(oldCtrs[i], newCtrs[i])
        if stopDist < 5:
            stopCrit = True

        stepCount = stepCount + 1

    print stepCount

if __name__ == "__main__":
    main()


