#Multivariate visualization
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target
plt.figure(figsize=(8,6))
sns.heatmap(df.iloc[:,:4].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix of Features")
plt.show()

plt.figure(figsize=(8,6))
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], s=df['petal length (cm)']*20, alpha=0.5,c=df['species'])
plt.title("Bubble chart of Sepal Length vs Sepal Width with Petal Length as Size")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.show()

sns.pairplot(df.iloc[:,:4])
plt.suptitle("Pair Plot of Features", y=1.02)
plt.show()