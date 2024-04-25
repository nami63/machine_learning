import numpy as np

# House sizes (in square feet)
X = np.array([1000, 1500, 2000, 2500, 3000])

# Corresponding house prices (in dollars)
y = np.array([300000, 400000, 500000, 600000, 700000])

from sklearn.linear_model import LinearRegression

# Reshape X to 2D array (required by scikit-learn)
X = X.reshape(-1, 1)

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict house prices for some new house sizes
new_sizes = np.array([[1200], [1800], [2200]])
predicted_prices = model.predict(new_sizes)

print("Predicted house prices:")
for size, price in zip(new_sizes, predicted_prices):
    print(f"House size: {size[0]} sqft, Predicted price: ${price:.2f}")
