# Standard t-tests (two tail):
 from scipy import stats
 a = [23,12,14,23,34,12,9,9,18,21,12,12,14,33,34,12,9,9,18,12] 
 b = [29,20,17,26,45,15,12,18,9,24,15,15,17,36,45,15,12,18,21,15] 
 t, pvalue = stats.ttest_ind(a,b)
 print "The t-statistic is %.3f and the p-value is %.3f." % (t,pvalue)
#The t-statistic is -1.413 and the p-value is 0.166Paired t-tests (two tail):

#paired t-tests (paired samples/dependent samples)
from scipy import stats
a = [23, 12, 14, 54, 34, 12, 9, 9, 18, 21]
b = [26, 15, 17, 57, 45, 15, 12, 18, 9, 24] 
t, pvalue = stats.ttest_rel(a,b) 
print "The paired t-statistic is %.3f and the p-value is %.3f." % (t,pvalue)
#The paired t-statistic is -1.945 and the p-value is 0.084
