import pandas as pd
import matplotlib.pyplot as plt

# Read data from the CSV file
df = pd.read_csv('filteredScores2022.csv')

# Filter data for India and Chad
countries_to_plot = ['India', 'Chad']
df_filtered = df[df['Country'].isin(countries_to_plot)]

# Select relevant columns
df_filtered = df_filtered[['Year', 'Country', 'Literacy', 'Gender gap in mobile ownership', 'Gender gap in mobile internet']]

# Convert percentages to decimal values
df_filtered['Literacy'] = df_filtered['Literacy'] / 100
df_filtered['Gender gap in mobile ownership'] = df_filtered['Gender gap in mobile ownership'] / 100
df_filtered['Gender gap in mobile internet'] = df_filtered['Gender gap in mobile internet'] / 100

# Plot the data
plt.figure(figsize=(10, 6))

for country in countries_to_plot:
    df_country = df_filtered[df_filtered['Country'] == country]
    plt.plot(df_country['Year'], df_country['Literacy'], label=f'{country} - Literacy', marker='o')
    plt.plot(df_country['Year'], df_country['Gender gap in mobile ownership'], label=f'{country} - Ownership Gap', marker='o')
    plt.plot(df_country['Year'], df_country['Gender gap in mobile internet'], label=f'{country} - Internet Gap', marker='o')

plt.title('Trends in Literacy and Gender Gaps (2022)')
plt.xlabel('Year')
plt.ylabel('Percentages')
plt.legend()
plt.grid(True)
plt.show()
