
#how many times we have the same words  
def count_val_3a(text,seq):
    count = 0
    for i in range(len(text)):
        if ''.join(text[i:len(seq)+i]) == seq:
            count += 1
    return count


count_val_3a(text1,'The')

#where is this word
def count_val_4(text,seq):
    positions = []
    for i in range(len(text)):
        if ''.join(text[i:(i+len(seq))]) == seq:  #we need if alpha is a list
            positions.append(i)
    return positions

count_val_4(text1,'t')
#calculate the positions of the space
def count_val_4(text1,seq):
    positions = []
    for i in range(len(text1)):
        if ''.join(text1[i:(i+len(seq))]) == seq:  #we need if alpha is a list
            positions.append(i)
    return positions

#calculate the mean value of time
positions=count_val_4(text1,' ')
mean=[]
for i in positions:
    mean.append(df1.final[:i].mean())

#calculate the std value of time
positions=count_val_4(text1,' ')
std=[]
for i in positions:
    std.append(df1.final[:i].std())


median=[]
for i in positions:
    median.append(df1.final[:i].median())

table=DataFrame({'mean_time':mean,'median_time':median,'std_time':std})


# alpha= long text string we have
#seq = is the word of interest
#return the positions  in the string

alpha='ABCDEFGHILMNOPQRSTUVZ'

def count_val_4(alpha,seq):
    positions = []
    for i in range(len(alpha)):
        if ''.join(alpha[i:(i+len(seq))]) == seq:  #we need if alpha is a list
            positions.append(i)
    return positions


#if we want to count how many times there is that word:
def count_val_3a(alpha,seq):
    count = 0
    for i in range(len(alpha)):
        if ''.join(alpha[i:len(seq)+i]) == seq:
            count += 1
    return count

 


