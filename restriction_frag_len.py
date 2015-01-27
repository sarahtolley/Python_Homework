#Restriction fragment lengths, exercise 3

my_dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

#find fragment lengths
frag1_length = my_dna.find("GAATTC") + 1
frag2_length = len(my_dna) - frag1_length

