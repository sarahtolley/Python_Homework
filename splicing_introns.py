#splicing out introns, parts 1-3, exercise 4

from __future__ import division 
my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"


#part 1
#designate exons in sequence
exon1 = my_dna[0:63]
exon2 = my_dna[90: ]
#print coding regions of the DNA sequence 
print("Part 1 : " + str(exon1 + exon2))

#part 2
#calculate what percentage of the DNA sequence is coding
coding_length = len(exon1 + exon2)
total_length = len(my_dna)
print("Part 2 : " + str(100 * coding_length / total_length))


#part 3
#splicing out introns
intron = my_dna[90: ]
print("Part 3 : " + str(exon1 +intron.lower() +exon2))
