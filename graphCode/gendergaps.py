import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('filteredScores2022.csv')

df = df[df['Year']==2022]

correlation_data = df[['Country', 'Gender Equality', 'Gender gap in mobile ownership', 'Gender gap in mobile internet']]


correlation_data = correlation_data.sort_values(by='Gender gap in mobile ownership')


correlation_data.set_index('Country', inplace=True)



plt.figure(figsize=(16, 8))
correlation_data.plot(kind='bar', colormap='Paired')
plt.title('Gender Metrics Comparison (by Country)')
plt.xlabel('Country')
plt.ylabel('Values')
plt.xticks(rotation=45)
plt.legend(title='Metrics', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()


for i, country in enumerate(correlation_data.index):
    plt.text(i, correlation_data.iloc[i].max() + 0.05, country, ha='center', va='bottom', rotation=45)

plt.show()
 