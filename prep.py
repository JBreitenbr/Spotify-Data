#import spielwiese,scrape,wrangle
#spielwiese.spiele(spielwiese.df1,spielwiese.df2)
#scrape.scrape(scrape.new)
#wrangle.wrangle(wrangle.df1,wrangle.df2,wrangle.bij)
import pandas as pd
s=pd.read_csv("spotiDaten3.csv")
#print(s.columns)
#print(s.iloc[987])
s["alphaname"]=s["alphaname"].astype(str)
#print(type(s.loc[987,"alphaname"]))

for i in range(len(s)):
  s.loc[i,"maiuscule"]=s.loc[i,"alphaname"].upper()[0]

mlst=s["maiuscule"].unique().tolist()
wlst=[]
for i in range(len(mlst)):
  wlst.append({})
for i in range(len(mlst)):
  wlst[i]["name"]=mlst[i]
  wlst[i]["bands"]=[]
blst=[]
for i in range(len(mlst)):
  hlp=s[s["maiuscule"]==mlst[i]]["artist"].unique().tolist()
  blst.append(hlp)
slst=[[] for i in range(len(mlst))]
for i in range(len(blst)):
  for j in range(len(blst[i])):
    slst[i].append({"name":blst[i][j]})
for i in range(len(wlst)):
  wlst[i]["bands"]=slst[i]
bands=pd.DataFrame(wlst)
bands.to_json("bandsObj.json",orient="records")

tracksObj={}
tracksObj["none"]=[{"artist":"none"}]
del s["alphaname"]
artists=s["artist"].unique().tolist()
for i in range(len(artists)):
  tracksObj[artists[i]]=[]
for artist in artists:
  sub=s[s["artist"]==artist]

  for j in range(len(sub)):
    sub.to_json("TracksData/{perf}.json".format(perf=artist),orient="records")

