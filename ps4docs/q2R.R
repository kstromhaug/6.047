library(tidyverse)
library(data.table)
library(dplyr)
library(reshape2)
library(lattice)
library(ggplot2)
library(stats)

pcaCharts <- function(x) {
  x.var <- x$sdev ^ 2
  x.pvar <- x.var/sum(x.var)
  print("proportions of variance:")
  print(x.pvar)
  
  par(mfrow=c(2,2))
  plot(x.pvar,xlab="Principal component", ylab="Proportion of variance explained", ylim=c(0,0.01), type='b')
  plot(cumsum(x.pvar),xlab="Principal component", ylab="Cumulative Proportion of variance explained", ylim=c(0,1), type='b')
  screeplot(x)
  screeplot(x,type="l")
  par(mfrow=c(1,1))
}

Exp_path = "ExpData.txt"

data = read.delim(Exp_path, sep='\t')
patients = data['Patient']
data$Patient <- NULL

# check data: 
head(data[,1:10])

# use princomp function

pca = prcomp(data)

loadings = pca$loadings[]
pca.variance.explained = pca$sdev^2 / sum(pca$sdev^2)

# plot percentage of variance explained for each principal component    
barplot(100*pca.variance.explained, las=2, xlab='', ylab='% Variance Explained')

plot1 = plot(pca)
plot2 = biplot(pca)

pcaCharts(pca)

comp = data.frame(pca$x[,1:3])

km = kmeans(comp, 2)

comp$cluster = as.factor(km$cluster)

ggplot(comp, aes(x=comp$PC1, y=comp$PC2, color=comp$cluster), xlim=c(-1,1), ylim=c(-1,1)) + geom_jitter()



