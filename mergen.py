import pandas as pd
bij=pd.read_csv("genred.csv")
df0=pd.read_csv("spotiDaten1.csv")
print(len(df0))
del df0["genres"]
df1=pd.merge(df0,bij,on="artist",how="left")
df1["alphaname"]=df1["alphaname_y"]
del df1["alphaname_y"]
del df1["alphaname_x"]
del df1["artist_id"]
print(df1.isnull().sum())
print(len(df1))
df1.to_csv("spotiDaten2.csv",index=False)