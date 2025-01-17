import pandas as pd
df1=pd.read_csv("spotiDaten2.csv")
df2=pd.read_csv("spieli2.csv")
bij=pd.read_csv("bij.csv")
#def wrangle(df1,df2,bij):
df2=pd.merge(df2,bij,on=["artist"],how="inner")
#del df2["artist_id"]
del df2["album_id"]
del df2["track_id"]
df=pd.concat([df1,df2])
df.reset_index(inplace=True)
for i in range(len(df)):
     df.loc[i,"year"]=df.loc[i,"album_date"][0:4]
for i in range(len(df)):
     su=df.loc[i,"track"]+" ("
     tr=df.loc[i,"album_tracks"]
     pos=tr.index(su)
     df.loc[i,"pos"]=pos
     df.sort_values(by=["alphaname","year","album_name","pos"],inplace=True)
del df["index"]
del df["year"]
del df["pos"]
df.to_csv("spotiDaten3.csv",index=False)
