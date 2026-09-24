#Bivariate vizuavalization
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target
plt.figure(figsize=(6,4))
sns.scatterplot(x=df['sepal length (cm)'], y=df['sepal width (cm)'], hue=df['species'])
plt.title("Scatter Plot of Sepal Length vs Sepal Width")
plt.show()

plt.figure(figsize=(6,4))
plt.plot(df['sepal length (cm)'])
plt.title("Line Plot of Sepal Length vs Sepal Width")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.show()

plt.figure(figsize=(6,4))
sns.barplot(x=df['species'], y=df['sepal length (cm)'])
plt.title("Bar Plot of Sepal Length by Species")
plt.xticks(ticks=[0, 1, 2], labels=iris.target_names)
plt.show()
