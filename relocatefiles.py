from shutil import copyfile
from sys import exit
import pandas as pd

df_index=pd.read_csv('/Users/mengjiexu/Documents/Projects/Twitter/AQ/secaaerpreta.csv')

for line in df_index["aaerno"]:
    source = "/Users/mengjiexu/Documents/Projects/Twitter/AQ/AAERtxt/%s.txt"%line.strip()
    target = '/Users/mengjiexu/Documents/Projects/Twitter/AQ/AAERpreTA/%s.txt'%line.strip()
    copyfile(source, target)