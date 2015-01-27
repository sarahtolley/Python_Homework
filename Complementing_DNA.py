#Complementing DNA, exercise 2

my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"


#replace my_dna with complement

replacement1 = my_dna.replace('A', 't') 
replacement2 = replacement1.replace('T','a')
replacement3 = replacement2.replace('C', 'g')
replacement4 = replacement3.replace('G', 'c')

#change complementary strand to uppercase
print(replacement4.upper())
