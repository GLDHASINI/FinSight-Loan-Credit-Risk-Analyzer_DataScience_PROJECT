#Bivariate vizuavalization
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")
plt.figure(figsize=(6,4))
sns.scatterplot(x=tips['total_bill'], y=tips['tip'], hue=tips['sex'])
plt.title("Scatter Plot of Total Bill vs Tip")
plt.show()

plt.figure(figsize=(6,4))
plt.plot(tips['total_bill'])
plt.title("Line Plot of Total Bill")
plt.xlabel("Sample Index")
plt.ylabel("Total Bill")
plt.show()

plt.figure(figsize=(6,4))
sns.barplot(x=tips['day'], y=tips['total_bill'])
plt.title("Bar Plot of Total Bill by Day")
plt.show()
