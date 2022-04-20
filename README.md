# phylogenetictools
handy scripts for performing phylogenetic analyses

# Concatenating fasta files of unequal length
For multi-gene analyses, my experience is not to have all genes for all taxa, especially when mining data on sources such as GenBank. I've done extensive searching some years ago to find a script that would be able to deal with this problem, i.e. merge a dataset with ~1000 ITS sequences with a dataset of ~500 LSU sequences, with partial overlap. Unfortunately, I wasn't able to find programs/scripts that could do this easily, so with a colleague (@Mike-Chester) I was able to create two sequential scripts to deal with this particular problem. Since, I have improved the second and final merge script to make sure it would add dashes '-' for the length of the alignments for the missing data. 

Planned are still to add argparse arguments in the scripts to facilitate usage, as well as merging the two scripts to simplify the process.
