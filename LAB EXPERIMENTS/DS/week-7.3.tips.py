#multivariate vizuavalization
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")
plt.figure(figsize=(8,6))
sns.heatmap(tips.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix of Numeric Features")
plt.show()

plt.figure(figsize=(8,6))
plt.scatter(tips['total_bill'], tips['tip'], 
            s=tips['size']*20, alpha=0.5, c=tips['size'])
plt.title("Bubble Chart of Total Bill vs Tip with Size as Bubble")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()

sns.pairplot(tips[['total_bill','tip','size']])
plt.suptitle("Pair Plot of Features", y=1.02)
plt.show()


# Advanced Techniques
plt.figure(figsize=(6,4))
sns.violinplot(x=tips['day'], y=tips['total_bill'])
plt.title("Violin Plot of Total Bill by Day")
plt.show()