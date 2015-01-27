#Restriction fragment lengths, exercise 3

my_dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

#find fragment lengths
frag1_length = my_dna.find("GAATTC") + 1
frag2_length = len(my_dna) - frag1_length

#print lengths
#need to use str() function to print numbers as a string 
print("length of fragment one is " + str(frag1_length))
print("length of fragment two is " + str(frag2_length))
