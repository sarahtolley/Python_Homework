#Complementing DNA, exercise 2

my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"


#replace my_dna with complement

replacement1 = my_dna.replace('A', 't')
#need to print it for the command to be useful
print(replacement1) 
replacement2 = replacement1.replace('T','a')
print(replacement2)
replacement3 = replacement2.replace('C', 'g')
print(replacement3)
replacement4 = replacement3.replace('G', 'c')
print(replacement4)

#change complementary strand to uppercase
print(replacement4.upper())
