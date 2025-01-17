import pandas as pd
df=pd.read_csv("bij.csv")
artists=df["artist"].unique().tolist()
char_tup=(("ü","ue"),(".",""),("'",""),("&","and"),(",",""),("ö","oe"),("ë","e"),("á","a"),("é","e"),("í","i"),("ó","o"),("13","t"),("35007","loose"),("-",""))
artDict={}

for i in range(len(artists)):
  art=artists[i].split(" ")
  for j in range(len(art)):
    art[j]=art[j].lower()
    for i1,i2 in char_tup:
      art[j]=art[j].replace(i1,i2)
  art2="_".join(art)
  artDict[artists[i]]=art2
artDict_rev={}
for k,v in artDict.items():
  artDict_rev[v]=k
import json
print(json.dumps(artDict_rev))