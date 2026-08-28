# Week 4 - Predictive Modeling and Optimization in Logistics Systems

 ## Project Overview

This project predicts logistics delivery time using machine learning and demonstrates a simple optimization strategy for selecting transport options.

A hypothetical dataset of 1,200 shipments is generated using Python. The target variable is delivery_time_days.

## Features

- region
- transport_mode
- warehouse
- shipment_volume_kg
- distance_km
- transport_cost

##Machine Learning Models
Two regression models are compared:
1. Linear Regression - provides a simple baseline and is easy to interpret.
2. Random Forest Regression - captures nonlinear relationships between shipment characteristics and delivery time.

## Evaluation Metrics
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R-squared
- 5-fold cross-validation MAE
The model with the lowest RMSE is selected as the best model.

## Optimization Strategy

The trained model predicts delivery time for different hypothetical transport options. A simple multi-objective score combines normalized transportation cost and predicted delivery time with equal weights:

Optimization Score = 0.5 × Cost + 0.5 × Delivery Time

Lower scores represent better trade-offs under this simulated objective.

## Technologies

Python, Pandas, NumPy, Scikit-learn, Matplotlib, Google Colab, GitHub

# Repository Structure

## Week-4-Predictive-Modeling-Optimization/
├── README.md
├── week4_predictive_optimization.py
└── requirements.txt

## How to Run in Google Colab

!pip install -q pandas numpy scikit-learn matplotlib
Then upload or paste week4_predictive_optimization.py into Colab and run it.
The script generates:
week4_logistics_dataset.csv
model_comparison.csv
optimized_transport_recommendations.csv

## Business Value

The project demonstrates how predictive analytics can estimate delivery time before dispatch. Logistics teams can use such predictions to compare transportation alternatives, identify potentially delayed shipments, and balance cost against service speed.

## Future Scope
- Hyperparameter tuning with GridSearchCV
- XGBoost or other ensemble models
- Real historical logistics data
- Route optimization
- Vehicle capacity optimization
- Demand forecasting
- Real-time ETA prediction

# Author
## Aditi Chaudhari 
