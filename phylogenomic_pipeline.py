# Import needed modules
import os
import sys
import glob
import subprocess
from Bio import SeqIO
from Bio.Seq import Seq
from Bio import Phylo

#COMMAND TO RUN FILE: 

#Store the path to the directory containing input files
##Note: We do not need to store every file, just need the ability to read them
in_dir = "/shared/forsythe/BB485/Week06/Brass_CDS_seqs/"

#Store the path to a new folder where we want to write the output
##Need the ability to write files here
out_dir = "/scratch/rehmanne/BB485/Weeks/Week_06/Out_Phylo_Pipeline/"

#Get a list of all fasta files in the input directory 
##Glob: glob.glob(<input directory> + "<search_string>")
all_in_files=glob.glob(in_dir + "*.fasta")
#print(all_in_files)


#***BEGINNING ALIGNMENT*** 

#Start a for-loop to loop through each file name: 
for file in all_in_files [0:10]:
    #print(file)

    #Create a new file path pointing to the output directory (how we tell mafft what to name the output)
    new_file_path = file.replace(in_dir, out_dir)
    #print(new_file_path)

    #Create a Mafft command for the file of interest
    aln_cmd = 'mafft --auto --quiet ' +file+ ' > ' + new_file_path
    #print(aln_cmd)
    #Call the mafft command from the command line using system call
    ##os.system: system call, runs this command as if from the command line
    os.system(aln_cmd)

#Create a for-loop to run iqtree
#Get a list of all fasta files in the input folder
all_aln_files=glob.glob(out_dir+"*.fasta")

#Blank list prior to for-loop
tree_list = []

#For loop to get align files and run iqtree on each (see example code and alter for my needs)
    #run tree_cmd using system call (try on command line first)


#For loop to go store each tree as a phylo object, getting a newick format
    #for loop to go through phylo object and see if "Es_" in tip name
    #break to store the loop once correct tip is found

#Root the tree using the outgroup(es_tip)

#Empty list for terminal (tips) branches

#For loop to save the names of the tips of each
    #if "Bs_"
        #save as Bs_temp
    #elif "Cr_"
        #save as Cr_temp
    #elif "At_"
        #store as At_temp
    #else
        #save as out_temp

#list of pairs of branches, this will allow us to which is monophyletic

#If/else to ask which is monophyletic using .is_monophyletic
    #When found, store as topo_str

#print(topo_str)
