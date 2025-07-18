# 🌾 Agri Price Predictor

A complete end-to-end Machine Learning web application that predicts the price of agricultural commodities like Onion, Potato, Chickpeas, etc., based on environmental and market factors. Built using Random Forest, Flask, and a custom HTML frontend.

---

## 📌 Features

- ✅ Train a Random Forest regression model on agricultural data
- ✅ Predict future commodity prices based on user inputs
- ✅ Accepts real-world features: temperature, rainfall, demand, supply, cost, season, etc.
- ✅ Clean and interactive web interface built with HTML + CSS
- ✅ Fully functional Flask API backend

---

## 🏗️ Project Structure
```
Agripricepredictor/
│
├── app/
│ ├── train_model.py # Trains the Random Forest model
│ ├── predict_api.py # Flask web app (frontend + backend)
│ └── templates/
│ └── index.html # Frontend UI form
│
├── data/
│ └── indian_agriculture_commodities.csv # Dataset
│
├── input.json # Sample input for POST testing
├── requirements.txt # List of Python dependencies
└── README.md # This file

```


---

## 🧠 Model Information

- **Algorithm**: Random Forest Regressor  
- **Target Variable**: Price per kg (₹)  
- **Performance (local)**:
  - RMSE: ~26.09
  - R² Score: ~-0.02 (initial model, can be improved)

---

## 🧪 Sample Input (JSON)

```json
{
  "State": "West Bengal",
  "District": "Kolkata",
  "Commodity": "Potato",
  "Season": "Winter",
  "Temperature (°C)": 22,
  "Rainfall (mm)": 20,
  "Supply Volume (tons)": 100,
  "Demand Volume (tons)": 120,
  "Transportation Cost (₹/kg)": 3.5,
  "Fertilizers Used (tons)": 50,
  "Pest Infestation": 2,
  "Market Competition": 7,
  "Year": 2025,
  "Month": 7,
  "Day": 18
}


```
## OUTPUT:

Predicted_Price: ₹48.15


---

## 🖼️ Demo Screenshot

![Web App Screenshot]()
![Web App Screenshot]()


## Acknowledgements

Developed as part of a Smart India Hackathon prototype

Dataset inspired by agricultural market monitoring systems

Mentorship & guidance from ChatGPT

---

## Future Improvements
```

Model accuracy improvement (hyperparameter tuning)

Add live charts using Chart.js

Deploy the app on Render/Heroku or Docker
```
