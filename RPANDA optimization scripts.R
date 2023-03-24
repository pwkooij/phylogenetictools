library(RPANDA)
library(phytools)

#load in tree
tree_in <- read.newick(file = "YOUR TREE")
plotTree(tree_in,fsize=0.6, no.margin=T) 

#root tree
outgroup <- c("YOUR OUTGROUP NAME")
tree_in <- root(tree_in, outgroup, resolve.root=TRUE)
plotTree(tree_in,fsize=0.6)

#creat chronogram with proportional branches
tree_in=chronos(tree_in, lambda=1)
plotTree(tree_in,fsize=0.6)

#RPANDA analyses to find optimum branching patterns
res<-spectR(tree_in)
plot_spectR(res)
res #res$eigengap -> gives autmated modalities, but not always most optimal

out<-capture.output(res)
cat(out,file=paste("YOUR SPECTR RESULTS",".txt",sep=""),sep="\n")#write away to .txt file

pdf(file="YOUR SPECTR RESULTS GRAPH.pdf")
plot_spectR(res)
dev.off()

#find optimum modality number
maxnum_mod <- 30

BICompare_test <- data.frame(matrix(ncol = 4, nrow = maxnum_mod))
X <-  c("tree BIC", "random BIC", "BIC ratio", "BSS/TSS")
colnames(BICompare_test) <- X
BICompare_test

for(i in 1:maxnum_mod) {
  output <- BICompare(tree_in,i)
  print(output)
  datavec <- c(output$BIC_test[,1], output$BIC_test[,2], (output$BIC_test[,1]/output$BIC_test[,2]), output$`BSS/TSS`)
  print(datavec)
  BICompare_test[i,] <- datavec
  print(BICompare_test)
}

#in table find best BSS/TSS
BICompare_test[BICompare_test$`BIC ratio` <= 0.25, ]
BICompare_test <- BICompare_test[order(BICompare_test$`BSS/TSS`, decreasing=T, na.last=T), ]
optimum_mod <- BICompare_test[1,1]

#compute BIC values assessing the support of modalities in phylogeny with optimum modality number
best_result <- BICompare(tree_in,optimum_mod)
num_repl <- 100 #choose number of replicates you want
total_result <- vector("list",length = num_repl)

for(r in 1:num_repl) {
  new_result <- BICompare(tree_in, optimum_mod)
  total_result[[r]] <- new_result 
  if (new_result$`BSS/TSS` > best_result$`BSS/TSS`) {
    best_result <- new_result
  }
  if (r %% 10 ==0) {
    cat(r, best_result$`BSS/TSS`, "\n")
  }
}

dev.off()

pdf(file="YOUR BICompare RESULTS GRAPH.pdf")
plot_BICompare(tree_in,best_result)
dev.off()

out<-capture.output(best_result)
cat(out,file=paste("YOUR BICompare RESULTS",".txt",sep=""),sep="\n")#write away to .txt file