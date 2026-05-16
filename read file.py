
import pandas as pd
#read file from local system
df = pd.read_csv('datamlbp.csv')

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded["datamlbp.csv"])))
  
#read the file into a pandas dataframe repalce 'filename.csv' with the name of your file
data_dict = pd.read_csv(io.BytesIO(uploaded['datamlbp.csv']))

#dispaly the first 5 rows of the dataframe to check if the data is loaded correctly
print(data_dict.head())


#1 empty cell
#remove empty cell
#return a new dataframe with empty cell
new_df = data_dict.dropna()
print(new_df.head())


#2fill empty cell
data_dict.fillna(0, inplace=True)



#3replace empty cell with mean mode or median
data_dict.fillna(data_dict.mean(), inplace=True)
data_dict.fillna(data_dict.mode(), inplace=True)
data_dict.fillna(data_dict.median(), inplace=True)
