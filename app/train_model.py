
import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import os

# Load the dataset
data = pd.read_csv('data/indian_agriculture_commodities.csv')

# Convert Date column to datetime and extract useful time features
data['Date'] = pd.to_datetime(data['Date'])
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month
data['Day'] = data['Date'].dt.day

# Drop original Date and separate target
X = data.drop(['Date', 'Price per kg (₹)'], axis=1)
y = data['Price per kg (₹)']

# One-hot encode categorical features
X = pd.get_dummies(X)

# Save column structure for prediction API
if not os.path.exists('model'):
    os.makedirs('model')
joblib.dump(list(X.columns), 'model/columns.pkl')

# Scale numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
joblib.dump(scaler, 'model/scaler.pkl')

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor()
model.fit(X_train, y_train)
joblib.dump(model, 'model/rf_model.pkl')

# Evaluate
y_pred = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))

r2 = r2_score(y_test, y_pred)

print(f" Model trained successfully!")
print(f" RMSE: {rmse:.2f}")
print(f" R² Score: {r2:.2f}")
