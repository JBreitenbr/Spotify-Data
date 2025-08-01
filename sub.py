import pandas as pd 
df0=pd.read_csv('spotiData_01Aug2025.csv')
cnt=df0["artist"].value_counts()
df=pd.merge(df0,cnt,on="artist")
print(len(df))
s=df[df["count"]>10]
s.to_csv("sub.csv",index=False)