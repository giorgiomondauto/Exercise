
import numpy.random as npr
npr.seed(123)
my_length = 100
bp = ['A','C','G','T']
DNA=''.join(npr.choice(bp,size=my_length))

1)
#Q1 The below function takes a DNA string and works out the number of times a certain letter appears. 
# Fill in the blanks to get the code to work for the below function call. (hint: the answer should be 25)
def count_val(dna,val):
    count = 0
    for i in dna:
        if i == val:
            count += 1
    return count
count_val(DNA,'A')
# is the same of dna.count("A")

2)
#The below function extends the previous one to allow for sequences of length two. However, there seems to be a mistake in the 4th line of the function. What should it read? (hint: the answer should be 7)
def count_val_2(dna,seq):
    count = 0
    for i in range(len(dna)):
	# Mistake is 
	#if ''.join(dna[i:(i+1)]) == seq:
        if ''.join(dna[i:(i+2)]) == seq:
            count += 1
    return count

count_val_2(DNA,'AA')
DNA = ''.join(npr.choice(bp,size=my_length))

3)
#Q3 The below function produces counts for sequences of undetermined length.
# Should be 
def count_val_3(dna,seq):
    count = 0
    for i in range(len(dna)):
        if ''.join(dna[i:(i+len(seq))]) == seq:
            count += 1
    return count
count_val_3(DNA,'AAAA')

4)
# PER LA POSIZIONE IN UNA STRINGA
npr.seed(123)
my_length = 10000
DNA = ''.join(npr.choice(bp,size=my_length))

def count_val_4(dna,seq):
    positions = []
    for i in range(len(dna)):
        if ''.join(dna[i:(i+len(seq))]) == seq:
            positions.append(i)
    return positions

count_val_4(DNA,'ACAGA') # [172, 2407, 3600, 6561, 7003, 7096]

4a)POSIZIONE CON DUE STRINGHE
# Q5 Write a function count_val_5 which takes 2 DNA strings of the same length and returns the number of times a set sequence occurs in both at the same location
def count_val_5(dna_1,dna_2,seq):
    count = 0
    for i in range(len(dna_1)):
        if (''.join(dna_1[i:(i+len(seq))]) == seq) & (''.join(dna_2[i:(i+len(seq))]) == seq):
            count = count+1
    print count

# Use your function on the following 2 DNA strings
npr.seed(123)
my_length = 100000
DNA_1 = ''.join(npr.choice(bp,size=my_length))
DNA_2 = ''.join(npr.choice(bp,size=my_length))
# Q5 How many times does the sequence ACA occur in both strings in the same place?
count_val_5(DNA_1,DNA_2,'ACA') # 22
