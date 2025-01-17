import pandas as pd
bij=pd.read_csv("bij.csv")
pt=bij[pd.notnull(bij["artist_id"])]
pt["l"]=pt["artist_id"].apply(lambda x: len(x))
sub=pt[pt["l"]!=22]
print(sub)
del pt["l"]
pt.to_csv(r"pt.csv",index=False)