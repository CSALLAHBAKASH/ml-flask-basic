import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error as mae, mean_squared_error as mse
import sklearn.datasets as ds
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Load the California housing dataset
data = ds.fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
target = pd.Series(data.target, name='target_variable')

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df, target, test_size=0.2, random_state=42)

# Create a pipeline with scaling and linear regression
pipeline = Pipeline([
    ('scaler', StandardScaler()),  # Scale features
    ('linear_regression', LinearRegression())
])

# Train the model
pipeline.fit(X_train, y_train)

# Evaluate the model
y_pred = pipeline.predict(X_test)
mae_score = mae(y_pred=y_pred, y_true=y_test)
mse_score = mse(y_pred=y_pred, y_true=y_test)
print(f"Mean Absolute Error: {mae_score}")
print(f"Mean Squared Error: {mse_score}")

# Save the model
joblib.dump(pipeline, 'reg_fetch_california_housing.joblib')

# Load the saved model
loaded_model = joblib.load('reg_fetch_california_housing.joblib')

# Make predictions using the loaded model
new_data = pd.DataFrame([[3.8462,52.0,6.281853,1.081081,565.0,2.181467,37.85,-122.25]], columns=data.feature_names)
predictions = loaded_model.predict(new_data)
print(predictions)
