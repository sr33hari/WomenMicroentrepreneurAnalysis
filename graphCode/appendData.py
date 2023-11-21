import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('filteredScores2022.csv')

df = df[df['Year']==2022]

df['Female_Literacy'] = None  
df['Income Gap'] = None


literacy = '64.01'
condition = df['Country'] == 'India'


df.loc[condition, 'Female Literacy'] = literacy
df.loc[condition, 'Income Gap'] = '0.58'

print(df)
