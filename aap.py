import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Step 1: Load the Data
file_path = r'C:/Users/Anas/Downloads/Data for house.xlsx'  # Update with your actual file path
data = pd.read_excel(file_path)

# Step 2: Define Features and Target
# Ensure these columns exist in your dataset: 'Rooms', 'Square Footage (sqft)', 'Price ($)'
features = data[['Rooms', 'Square Footage (sqft)']]  # Features
target = data['Price ($)']  # Target variable (what we want to predict)

# Step 3: Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Step 4: Initialize and Train the Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Make Predictions on the Test Set
predictions = model.predict(X_test)

# Step 6: Evaluate the Model
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = mse ** 0.5

print("Model Evaluation:")
print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)

# Step 7: Example Prediction with New Data
# Define new data with the same features to make a price prediction
new_data = pd.DataFrame({
    'Rooms': [3],  # Example: 3 rooms
    'Square Footage (sqft)': [1500]  # Example: 1500 sqft
})

# Predict the price for this new data
predicted_price = model.predict(new_data)
print("Predicted Price for new data ($):", predicted_price[0])
