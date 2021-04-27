import pandas as pd
import re,os
import twint
from tqdm import tqdm
import nest_asyncio
nest_asyncio.apply()

# Working directory
root_list = ["E:\\Dropbox\\Voice_paper\\empirical\\0_data\\external\\",
             "D:\\Syncfolder\\Dropbox\\Voice_paper\\empirical\\0_data\\external\\"]
def root_directory(x):
    for q in x:
        if os.path.exists(q):
            y=q
    return y
root_path = root_directory(root_list)
if 'root_path' not in globals():
    print('add your dropbox path after line 21') # dropbox directory
print(root_path)

df_l=pd.read_csv(root_path+ 'legislator_tw.csv')
df=pd.DataFrame(columns=['id','twitter'])

re_id = re.compile(r'\'bioguide\':\s*\'(\S*)\'')
re_twitter= re.compile(r'\'twitter\':\s*\'(\S*)\'')


df['id']=df_l['id'].str.extract(r'\'bioguide\':\s*\'(\S*)\'',expand=False)
df['twitter']=df_l['social'].str.extract(r'\'twitter\':\s*\'(\S*)\'',expand=False)
index=0

for id in tqdm(df['twitter']):
    try:
        c = twint.Config()
        name_id= df.iloc[index,1]
        c.Username = id
        c.Store_csv = True
        c.Output = root_path+'legislator tweets//'+ name_id+'.csv'
        c.Lang = "en"
        c.Hide_output =True
        twint.run.Search(c)
    except:
        continue
    index+=1                                                                 
