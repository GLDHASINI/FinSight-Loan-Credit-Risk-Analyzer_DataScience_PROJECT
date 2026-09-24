import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")


# Univariate Visualizations
plt.figure(figsize=(6,4))
sns.histplot(tips['total_bill'], bins=20, kde=True)
plt.title("Histogram of Total Bill")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x=tips['total_bill'])
plt.title("Box Plot of Total Bill")
plt.show()

day_counts = tips['day'].value_counts()
plt.figure(figsize=(6,4))
plt.pie(day_counts, labels=day_counts.index, autopct='%1.1f%%')
plt.title("Pie Chart of Day Distribution")
plt.show()



