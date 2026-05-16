import dataframe as df
#1 empty cell
#remove empty cell
#return a new dataframe with empty cell
new_df = df.dropna()
print(new_df.head())


#2fill empty cell
df.fillna(0, inplace=True)



#3replace empty cell with mean mode or median
x = df.mean()
df.fillna(df.mean(), inplace=True)
x = df.mode()
df.fillna(df.mode(), inplace=True)
x = df.median()
df.fillna(df.median(), inplace=True)
