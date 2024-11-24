
# **House Predictor Backend**

This repository contains the backend implementation for a machine learning-powered house price prediction system. It provides RESTful API endpoints to predict house prices based on input features like bedrooms, bathrooms, square footage, grade, and neighborhood rank.

---

## **Features**
- **House Price Prediction**: Predicts the price of a house using a pre-trained Random Forest model.
- **Validation**: Ensures input data is within acceptable ranges to maintain model accuracy.
- **Cluster Data API**: Provides access to cluster summary data for further analysis.
- **CORS Enabled**: Supports cross-origin requests to integrate with frontend applications.

---

## **Technologies Used**
- **Backend Framework**: Flask
- **Modeling and Data Processing**: Scikit-learn, Pandas
- **Serialization**: Pickle
- **API Testing**: Postman or cURL
- **Deployment**: Compatible with cloud platforms (e.g., Heroku, AWS)

---

## **Endpoints**

### **1. POST /predict**
Predicts the price of a house based on input features.
- **Input (JSON):**
  ```json
  {
    "bedrooms": 3,
    "bathrooms": 2,
    "sqft_living": 1500,
    "grade": 7,
    "yr_built": 1995,
    "yr_renovated": 2005,
    "neighborhood_rank": 8
  }
  ```
- **Output (JSON):**
  ```json
  {
    "predicted_price": 450000
  }
  ```
- **Error Response (JSON):**
  ```json
  {
    "error": "Invalid value for bathrooms: 15"
  }
  ```

---

### **2. GET /api/clusters**
Returns the cluster summary data from the `cluster_summary.csv` file.
- **Response (JSON):**
  ```json
  [
    {
      "Cluster": 1,
      "Average Price": 450000,
      "Average Sqft": 1800
    },
    {
      "Cluster": 2,
      "Average Price": 750000,
      "Average Sqft": 2200
    }
  ]
  ```
- **Error Response:**
  - `404`: File not found.
  - `500`: Unexpected server error.

---

### **3. GET /api/test**
A test route to check if the API is running.
- **Response (JSON):**
  ```json
  {
    "message": "API is working"
  }
  ```

---

## **Setup Instructions**

### **Clone the Repository**
```bash
git clone https://github.com/your-username/house_predictor_backend.git
cd house_predictor_backend
```

### **Create and Activate a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # For Linux/MacOS
venv\Scripts\activate     # For Windows
```

### **Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Run the Application**
```bash
python app.py
```

### **Access the API**
- The API will be available at: `http://127.0.0.1:5000/`

---

## **Folder Structure**
```
house_predictor_backend/
│
├── app.py                 # Main application file
├── optimized_rf_model.pkl # Trained Random Forest model
├── cluster_summary.csv    # CSV containing cluster data
├── requirements.txt       # Python dependencies
├── index.html             # Placeholder for potential frontend integration
├── venv/                  # Virtual environment folder
├── node_modules/          # Node.js modules (if required for future features)
```

---

## **Future Enhancements**
- Add user authentication for secure API access.
- Deploy the backend on a cloud platform (e.g., AWS or Heroku).
- Integrate with a frontend for a complete web application.
- Extend the `/predict` endpoint to return confidence intervals.

---

## **Contributing**
Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Contact**
- **Author**: Nafisat Ibrahim
- **Email**: nafisat.l@outlook.com
- **GitHub**: https://github.com/Nafisatibrahim/house_predictor_backend
