
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

tips = pd.read_csv('https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/reshape2/tips.csv')

# Data set comes from the R reshape2 package - see also references therein
# Contains a load restaurant bills wiht the tip, the sex of the payee, whether
# they smoked, the day, the time, and the size of the party

# Have a look at it:
tips.head()

# Create a new column containing the percentage tip
tips['pct'] = tips.tip/tips.total_bill

# Suppose I now want to see whether males or females tip more on average
# One way of doing it
tips.pct[tips.sex=='Female'].mean()
tips.pct[tips.sex=='Male'].mean()
# Females tip slightly more

# A more elegant way is to create a grouped by object
tips_gr = tips.pct.groupby(tips.sex)
# This doesn't contain anything obvious:
tips_gr

# But now you can access things with it:
tips_gr.mean()
tips_gr.std()
# Other functions you can use include count, sum , median, min/max, etc
# See tips_gr.<Tab> for lots more

# If you're interested in multiple variables you can do this too
tips_gr_2 = tips.groupby('sex')
tips_gr_2.median()

# You don't have to group by just one variable
tips_gr_3 = tips.groupby(['sex','smoker'])
tips_gr_3.describe()
tips_gr_3.mean()

# Note that tips_gr_3 has a hierarchical index of both smoker and sex
# You can get re-arrange this with
tips_gr_3.mean().unstack()
# or
tips_gr_3.mean().unstack(level=0)
# Note the difference, the first adds smoker to the columns whilst the second
# adds sex - both are still hierarchical indexes

# Unstack is often more useful if you have just one variable with a hierarchical
# index:
tips_gr_4 = tips.pct.groupby([tips.sex,tips.smoker])
tips_gr_4.mean()
tips_gr_4.mean().unstack() # Turns it into a nice DataFrame with no hierarchical index

# You can actually pass any Series function to a grouped by object
def IQR(x):
    return x.quantile(0.75)-x.quantile(0.25)
    
# You just need to provide it to the agg method
tips.groupby(['sex','smoker']).agg(IQR)

# You can use agg to get fancier tables of results
tips.groupby(['sex','smoker']).agg(['count','mean','std'])

# You can even run different functions for different columns by providing a dict
tips.groupby(['sex','smoker']).agg({'total_bill':'count','tip':'mean','size':'std'})

# Or even more complicated!
tips.groupby(['sex','smoker']).agg({'total_bill':'count','tip':['mean','min','max'],'size':'std'})
