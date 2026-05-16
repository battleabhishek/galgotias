#print dataframe eg
import pandas as pd

print("pandas dataframe example")

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 45],    
        'marks': [85, 90, 95, 80, 75]}

df = pd.DataFrame(data)
print("dataframe:\n", df)
print("data:", data)
