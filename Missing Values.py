
## Pandas and missing data

# As stated in lecture 5, pandas uses NaN as a missing value
# NaN stands for Not a Number
# You can use the NumPy nan or the Python None value to insert them in a Series or Data Frame
salary = Series([53215,112454,22365,np.nan,30493,None],index=['Margaret','Stephen','Joanne','Joe','Matthew','Nelson'])

# Note that by default all the above summary functions remove NaNs
salary.mean()

# When sorted, NaNs are treated as arbitrarily large
salary.order()

# The isnull method will tell you whether something is missing
salary.isnull()
# notnull will tell you the opposite
salary.notnull()

# Two other useful ways of dealing with missing values is to drop them (dropna) or fill in values (fillna)
# Compare
salary.dropna().mean()
# with
salary.fillna(0).mean()

# When you have a DataFrame things get a bit messier - do you want to drop all the rows with NAs or just some of them?
salary = DataFrame({'salary':[53215, 112454, 22365, np.nan, 30493, None],
    'grade':[5, 7, None, np.nan, 2, 9]},index=['Margaret', 'Stephen', 'Joanne', 'Joe', 'Matthew', 'Nelson'])

# Drop NA drops all rows with NAs - this permits complete case analysis
salary.dropna()

# Changing the how argument to 'all' only drops rows that are all NaN
salary.dropna(how='all')

# fillna will work on DataFrames too
salary.fillna(0)

# Giving fillna a dict will fill in each column
salary.fillna({'grade':4,'salary':10000})

# Note that fillna creates a new object, but you can overwrite the existing one with the argument inplace
#salary.fillna({'grade':4,'salary':10000},inplace=True)

# Why not impute the missing values with the column mean?
salary.fillna(salary.mean())

my_missing_2 = {'cut':'-1','clarity':'NaN','price':['NULL','-999'],'y':'NaN'}
dia_5a = pd.read_csv(path+'diamonds_4.csv',na_values=my_missing_2)



