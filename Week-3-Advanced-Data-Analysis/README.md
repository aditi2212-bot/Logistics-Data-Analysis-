# Week 3 - Advanced Data Analysis and Visualization in Logistics

## Overview
This project performs exploratory data analysis and visualization on a hypothetical logistics dataset. The dataset simulates shipment volume, delivery time, transportation cost, distance, fuel cost, region, warehouse, transport mode, and on-time delivery performance.

## Objectives
- Perform exploratory data analysis
- Calculate descriptive statistics and central tendencies
- Study distributions and correlations
- Identify cost drivers and possible delivery bottlenecks
- Create interactive visualizations using Plotly
- Translate analytical results into logistics recommendations

## Dataset
A hypothetical dataset containing 1,000 shipment records is generated automatically by Python. It includes shipment ID, region, transport mode, warehouse, shipment volume, delivery time, distance, transport cost, fuel cost, and on-time delivery.

## Visualizations
1. Delivery time distribution
2. Average transport cost by mode
3. Shipment volume vs delivery time
4. Correlation matrix
5. On-time delivery rate by region

## Technologies
Python, Pandas, NumPy, Plotly, Google Colab, GitHub

## Repository Structure
```text
Week-3-Advanced-Data-Analysis/
├── README.md
├── week3_analysis.py
└── requirements.txt
```

## How to Run in Google Colab
```python
!pip install -q pandas numpy plotly
```
Then upload or paste `week3_analysis.py` into Colab and run it. The script generates the hypothetical data and saves `week3_logistics_analysis.csv`.

## Business Value
The analysis helps compare transportation modes, understand delivery-time patterns, investigate cost drivers, and identify regions that may need operational attention.

## Future Scope
The project can be extended to delivery-time prediction, demand forecasting, shipment clustering, warehouse optimization, and route optimization.

## Author
Your Name
