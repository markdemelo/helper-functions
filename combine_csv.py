import pandas as pd
import os

files = os.listdir()
# print(files)
csv_files = []
cols = ["Date","Date entered","Reference","Description","Amount"]
df = pd.DataFrame(columns = cols)

for file in files:
    if file.endswith(".csv"):
        # print(file)
        # csv_files.append(file)
        new_df = pd.read_csv(file)
        # print(new_df)
        df = pd.concat([df,new_df])
    else:
        pass

df.to_excel("Statements for MBNA CC.xlsx")
        

  
    