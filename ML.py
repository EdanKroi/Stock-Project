import client
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

prices = client.closelist # prices is the closing set of the stock coke for this year 


data = pd.DataFrame({
    'Day': np.arange(len(prices)),  # Feature: Day (or time step)
    'Price': prices  # Target: Price
})

# Display the first few rows
print(data.head()) 

X = data[['Day']]  # Feature
y = data['Price']  # Target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print(predictions)

from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

plt.figure(figsize=(10, 5))
plt.scatter(X_test, y_test, color='blue', label='Actual Prices')
plt.scatter(X_test, predictions, color='red', label='Predicted Prices')
plt.xlabel('Day')
plt.ylabel('Price')
plt.title('Actual vs Predicted Prices')
plt.legend()
plt.grid(True)
plt.show()