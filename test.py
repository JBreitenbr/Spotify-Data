import pandas as pd 
df=pd.read_csv("sub.csv")[["artist","count"]]
df.drop_duplicates(inplace=True)
df.reset_index(inplace=True)
df.set_index('artist').rename(columns={'count':'cnt'})["cnt"].to_json('countDict.json')
