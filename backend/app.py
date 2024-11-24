from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd

# Load the model
with open('optimized_rf_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialize Flask app
app = Flask(__name__)
#CORS(app)  # Enable CORS for all routes
CORS(app, resources={r"/*": {"origins": "https://nafisatibrahim.github.io"}})

# Define feature names and acceptable ranges
feature_names = ['bedrooms', 'bathrooms', 'sqft_living', 'grade', 
                 'yr_built', 'yr_renovated', 'neighborhood_rank']
feature_ranges = {
    'bedrooms': (0, 10),
    'bathrooms': (0, 10),
    'sqft_living': (1, float('inf')),  # sqft_living should be greater than 0
    'grade': (1, 10),
    'yr_built': (1800, 2023),  # assuming a reasonable year range
    'yr_renovated': (0, 2023),  # 0 for not renovated
    'neighborhood_rank': (1, 10)
}

def validate_input(data):
    """Validate the input data."""
    for feature, (min_val, max_val) in feature_ranges.items():
        if feature not in data:
            return False, f"Missing feature: {feature}"
        if not (min_val <= data[feature] <= max_val):
            return False, f"Invalid value for {feature}: {data[feature]}"
    return True, None

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from request
    data = request.get_json()

    # Validate input data
    is_valid, error_message = validate_input(data)
    if not is_valid:
        return jsonify({'error': error_message}), 400

    # Extract features and ensure the order matches the model's expectation
    features = [
        data['bedrooms'], data['bathrooms'], data['sqft_living'], 
        data['grade'], data['yr_built'], data['yr_renovated'], 
        data['neighborhood_rank']
    ]

    # Convert the input data to a DataFrame
    input_df = pd.DataFrame([features], columns=feature_names)

    try:
        # Make prediction using the model
        prediction = model.predict(input_df)[0]
        return jsonify({'predicted_price': prediction})
    except Exception as e:
        # Catch any unexpected errors during prediction
        return jsonify({'error': f"An error occurred during prediction: {str(e)}"}), 500

# New route to serve cluster data
@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({"message": "API is working"})

@app.route('/api/clusters', methods=['GET'])
def get_clusters():
    print("Attempting to access cluster_summary.csv")  # Debug statement
    try:
        # Load cluster data from CSV
        cluster_data = pd.read_csv('cluster_summary.csv')  # Path appears correct
        print("File loaded successfully")  # Debug statement
        clusters_json = cluster_data.to_dict(orient='records')
        return jsonify(clusters_json)
    except FileNotFoundError:
        print("File not found")  # Debug statement
        return jsonify({'error': 'Cluster summary file not found'}), 404
    except Exception as e:
        print(f"An error occurred: {str(e)}")  # Debug statement
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500

"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

# Load the model
with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from request
    data = request.get_json()

    # Extract features from JSON
    features = [
        data['bedrooms'], data['bathrooms'], data['sqft_living'], 
        data['sqft_lot'], data['floors'], data['waterfront'], data['view'],
        data['condition'], data['grade'], data['sqft_above'], 
        data['sqft_basement'], data['yr_built'], data['yr_renovated'], 
        data['zipcode'], data['lat'], data['long'], data['sqft_living15'], 
        data['sqft_lot15']
    ]

    # Make prediction
    prediction = model.predict([features])[0]

    # Return the prediction as JSON
    return jsonify({'predicted_price': prediction})

if __name__ == '__main__':
    app.run(debug=True)

 """
