import matplotlib.pyplot as plt

# Data from the article
statistics = [
    ("Primary Girls Out of School (%)", 30),
    ("Learners without Computers (%)", 89),
    ("Learners without Internet Access (%)", 82)
]

# Extract labels and values
labels, values = zip(*statistics)

# Create a horizontal bar chart
plt.figure(figsize=(10, 6))
plt.barh(labels, values, color=['blue', 'green', 'red'])
plt.xlabel('Percentage')
plt.title('Education Disparities in Africa')

# Add text labels for each bar
for i, v in enumerate(values):
    plt.text(v + 2, i, str(v) + '%', va='center', color='black', fontweight='bold')
plt.tight_layout()
plt.show()
