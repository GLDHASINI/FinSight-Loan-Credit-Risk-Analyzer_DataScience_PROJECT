import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression

# LINEAR REGRESSION
print("----- Linear Regression -----")
# Independent Variable (House Size in square feet)
X_linear = np.array([[1000], [1200], [1500], [1800], [2000]])
# Dependent Variable (House Price in lakhs)
y_linear = np.array([50, 55, 65, 80, 90])
# Create Linear Regression model
linear_model = LinearRegression()
# Train model
linear_model.fit(X_linear, y_linear)
# Predict price for new house
new_house_size = np.array([[1700]])
predicted_price = linear_model.predict(new_house_size)
print("Training House Sizes:")
print(X_linear.flatten())
print("\nTraining House Prices:")
print(y_linear)
print("\nPredicted Price for 1700 sq.ft house:")
print(predicted_price[0])
