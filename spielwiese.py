import pandas as pd
df1=pd.read_csv("spotiDaten2.csv")
df2=pd.read_csv("new.csv")
#def spiele(df1,df2):
mrg=pd.merge(df1,df2,on= ["artist","track"],how="right")
print(mrg.isnull().sum())
droplist=[]
for i in range(len(mrg)):
    if not pd.isnull(mrg.loc[i,"alphaname"]):
         droplist.append(i)
mrg.drop(droplist,inplace=True)
mrg[["track_id","album_id","artist_id","artist","track"]].to_csv("spieli.csv",index=False)
