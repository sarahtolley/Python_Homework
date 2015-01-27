#AT content, exercise 1

from __future__ import division

my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"


#count A and T
length = len(my_dna)
a_count = my_dna.count('A')
t_count = my_dna.count('T')

#print number of A and T
at = (a_count + t_count) / length
print("AT content is " + str(at))
