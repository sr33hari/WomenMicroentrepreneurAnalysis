import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('filteredScores2022.csv') 


df_2022 = df[df['Year'] == 2022]


plt.figure(figsize=(14, 8))
plt.bar(df_2022['Country'], df_2022['Mobile download speeds'], color='blue')
plt.title('Mobile Download Speeds in 2022')
plt.xlabel('Country')
plt.ylabel('Download Speed (Mbps)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df_2022['Network coverage'], df_2022['Affordability'], alpha=0.5, color='green')
plt.title('Affordability vs. Network Coverage (2022)')
plt.xlabel('Network Coverage')
plt.ylabel('Affordability')


for i, country in enumerate(df_2022['Country']):
    plt.text(df_2022['Network coverage'].iloc[i], df_2022['Affordability'].iloc[i], country, fontsize=8)

plt.tight_layout()
plt.show()
