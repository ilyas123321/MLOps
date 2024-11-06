import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Update file path to reflect the new file name
file_path = 'rent_house_data.xlsx'  # Use the relative path for the updated file name
data = pd.read_excel(file_path)

# Define features and target
features = data[['Rooms', 'Square Footage (sqft)']]  # Features
target = data['Price ($)']  # Target variable (what we want to predict)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions using the test data
predictions = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = mse ** 0.5

# Print the model evaluation metrics
print("Model Evaluation:")
print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)

# Example of new data for prediction (3 rooms and 1500 sqft)
new_data = pd.DataFrame({
    'Rooms': [3],  # Example: 3 rooms
    'Square Footage (sqft)': [1500]  # Example: 1500 sqft
})

# Predict the price for the new data
predicted_price = model.predict(new_data)
print("Predicted Price for new data ($):", predicted_price[0])
