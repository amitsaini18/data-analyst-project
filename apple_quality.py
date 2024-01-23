import pandas as pd
import scipy.stats as stats
df=pd.read_csv("c:\\apple_quality.csv")
print(df.head())
print(df.isnull().sum())
print("Dropping the null values from data set...")
df.dropna(axis=0, inplace=True)
print(df.isnull().sum())

print("Need to check outlier for each numerical field.lets start with apple size")
df['Size_zscore']=stats.zscore(df['Size'])
print("Remove Outlier for Size ")
df['outlier']=df['Size_zscore'].apply(lambda x: 'True' if x>3 else 'False')
print(df.head())
#print(df['Size'])