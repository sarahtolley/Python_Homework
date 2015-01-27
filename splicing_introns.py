#splicing out introns, parts 1-3, exercise 4

from __future__ import division 
my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"


#part 1
#designate exons in sequence
exon1 = my_dna[0:63]
exon2 = my_dna[90: ]
#print coding regions of the DNA sequence 
print(exon1 + exon2)

#part 2
#calculate what percentage of the DNA sequence is coding
coding_length = len(exon1 + exon2)
total_length = len(my_dna)
print(100 * coding_length / total_length)


