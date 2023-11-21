import matplotlib.pyplot as plt

# Data from the article
internet_usage = 24
online_shopping = 24
cash_transactions = 95

# Create a bar chart to visualize internet usage
categories = ['Internet Usage (%)', 'Online Shopping (%)', 'Cash Transactions (%)']
values = [internet_usage, online_shopping, cash_transactions]

plt.figure(figsize=(10, 6))
plt.bar(categories, values, color=['blue', 'green', 'red'])
plt.xlabel('Categories')
plt.ylabel('Percentage')
plt.title('Digital Adoption in Africa')
plt.ylim(0, 100)  # Set y-axis limit to 0-100 for percentage values

# Add text labels for each bar
for i, v in enumerate(values):
    plt.text(i, v + 1, str(v) + '%', ha='center', va='bottom')

plt.show()
