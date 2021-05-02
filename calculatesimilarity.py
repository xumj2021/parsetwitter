import distance
import pandas as pd

df = pd.read_csv("/Users/mengjiexu/Documents/Projects/Twitter/AQ/cikmeta.csv",header=0)

def similar(a, b):
   return distance.levenshtein(a, b)

similarity = [similar(df['FirmName'][i].lower(), df['CikRelatedName'][i].lower()) for i in range(len(df))]
df['LevenshteinSimilarity'] = similarity

df.to_csv("/Users/mengjiexu/Documents/Projects/Twitter/AQ/cikmetawithsimilarity.csv",index=None)