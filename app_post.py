# Sample data (Now send the request AFTER the app is running)
data = {
    "features": [3.8462, 52.0, 6.281853, 1.081081, 565.0, 2.181467, 37.85, -122.25],
    "feature_names": ["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup", "Latitude", "Longitude"]
}

import requests
# Send the POST request
response = requests.post("http://127.0.0.1:5000/predict", json=data)

# Check the response
if response.status_code == 200:
    print(response.json())  # Print the prediction
else:
    print(f"Error: {response.status_code}")

"""
curl -X POST -H "Content-Type: application/json" -d '{
  "features": [3.8462,52.0,6.281853,1.081081,565.0,2.181467,37.85,-122.25],
  "feature_names": ["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup", "Latitude", "Longitude"]
}' http://localhost:5000/predict
"""

# GET:      curl -X GET http://localhost:5000
# POST:     curl -X POST -H "Content-Type: application/json" -d '{"key": "value"}' http://localhost:5000/data
# PUT:      curl -X PUT -H "Content-Type: application/json" -d '{"key": "updated_value"}' http://localhost:5000/data/1
# DELETE:   curl -X DELETE http://localhost:5000/data/1