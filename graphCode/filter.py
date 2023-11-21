import pandas as pd

def filter_data_by_countries(data_file, countries):

    df = pd.read_csv(data_file)


    filtered_data = df[df['Country'].isin(countries)]
    # filtered_data = df[df['Year']==2022]
    return filtered_data

countries_to_filter = [
    'Eritrea', 'Burundi', 'Central African Republic', 'Chad', 'Congo Democratic Republic', 
    'Equatorial Guinea', 'Mozambique', 'Liberia', 'Afghanistan', 'Mauritania', 'Burkina Faso', 
    'South Sudan', 'Niger', 'Sudan', 'Guyana', 'Tuvalu', 'Cuba', 'Solomon Islands', 'Gambia', 
    'Papua New Guinea', 'Namibia', 'Somalia', 'Djibouti', 'Libya', 'Pakistan', 'Sierra Leone',
    'Bangladesh', 'Indonesia', 'Bhutan', 'Nepal', 'India', 'Laos', 'Myanmar', 'Pakistan', 'Sri Lanka', 'Timor-Leste','United States of America'
]

data_file_path = 'indexScores.csv'

filtered_data = filter_data_by_countries(data_file_path, countries_to_filter)

filtered_data.to_csv("filteredScores2022.csv")


#create a list of prime numbers
prime = []