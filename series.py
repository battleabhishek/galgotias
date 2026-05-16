# read data from xml files in series dataframe
import pandas as pd

print("pandas seresies example")
data= {10,20,30,40,50}
series = pd.Series(data)

print("list of data:", data)
print("conerted to pandas series:", pd.Series(data))
print("series:", series)
