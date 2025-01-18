import json
artDict=json.load(open("artists.json"))
artLst=artDict["artists"]

hDict1={}
for art in artLst:
  hDict1[art]=art+"/"
print(hDict1)

  