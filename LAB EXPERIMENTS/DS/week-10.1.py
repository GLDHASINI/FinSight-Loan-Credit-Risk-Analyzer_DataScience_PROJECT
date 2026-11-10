import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
print("\n\n----- Logistic Regression -----")
# Independent Variable (House Price in lakhs)
X_logistic = np.array([[40], [50], [60], [70], [80], [90]])

# Dependent Variable
# 0 = Not Purchased
# 1 = Purchased
y_logistic = np.array([0, 0, 0, 1, 1, 1])
# Create Logistic Regression model
logistic_model = LogisticRegression()
# Train model
logistic_model.fit(X_logistic, y_logistic)
# Predict whether customer will purchase
test_price = np.array([[75]])
purchase_prediction = logistic_model.predict(test_price)
# Probability prediction
purchase_probability = logistic_model.predict_proba(test_price)
print("Training House Prices:")
print(X_logistic.flatten())
print("\nPurchase Labels:")
print(y_logistic)
print("\nTest House Price:", test_price[0][0])
print("\nPurchase Prediction:")
print(purchase_prediction[0])
print("\nPrediction Probabilities:")
print(purchase_probability)
