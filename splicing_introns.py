#splicing out introns, parts 1-3, exercise 4

my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

#part 1
#designate exons in sequence
exon1 = my_dna[0:63]
exon2 = my_dna[90: ]
#print coding regions of the DNA sequence 
print(exon1 + exon2)

