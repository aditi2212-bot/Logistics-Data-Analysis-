# Week 1 - Strategic Planning and Data Exploration in Logistics

## Project Overview

This project focuses on the strategic planning and initial data exploration phase of a logistics data analysis project.

The project uses customer and geographic data from the Olist Brazilian E-Commerce Public Dataset. The objective is to understand customer distribution across cities and states and explore how this information can support logistics planning and resource allocation.

Interactive visualizations are used to explore customer concentration and geographic distribution.

## Logistics Scenario

An e-commerce company wants to understand where its customers are geographically concentrated.

Customer geographic information can help logistics teams:

- Identify high-demand regions
- Plan distribution resources
- Identify important customer markets
- Support warehouse location planning
- Improve regional logistics planning
- Prepare for future route optimization

## Objectives

The main objectives of this project are:

1. Understand the customer dataset.
2. Explore customer geographic distribution.
3. Calculate important logistics-related KPIs.
4. Identify states and cities with high customer concentration.
5. Create interactive visualizations.
6. Develop a roadmap for future logistics analysis.

## Dataset

The project uses two datasets from the Olist Brazilian E-Commerce Public Dataset:

- `olist_customers_dataset.csv`
- `olist_geolocation_dataset.csv`

The customer dataset contains:

- Customer ID
- Unique customer ID
- ZIP-code prefix
- City
- State

The geolocation dataset contains:

- ZIP-code prefix
- Latitude
- Longitude
- City
- State

The geolocation dataset is used to connect customer ZIP-code prefixes with geographic coordinates.

## Dataset Source

Olist Brazilian E-Commerce Public Dataset:

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

The datasets are not included in this GitHub repository.

## Key Performance Indicators

### Total Customer Records

The total number of customer records available in the dataset.

### Unique Customers

The number of unique customers based on `customer_unique_id`.

### Number of States

The number of states represented in the customer dataset.

### Number of Cities

The number of unique cities represented in the dataset.

### Customer Concentration

The percentage of customers located in each state.

## Data Science Approach

### Exploratory Data Analysis

Customer data is explored to identify:

- Customer distribution by state
- Customer distribution by city
- Geographic concentration
- High-volume customer regions

### Clustering

In future analysis, clustering techniques such as K-Means can be used to group regions according to customer concentration and logistics requirements.

### Optimization

Customer geographic information can later be combined with order, seller, and delivery data to support:

- Warehouse location planning
- Distribution planning
- Route optimization
- Resource allocation

## Interactive Visualizations

The project uses Plotly to create interactive visualizations.

The analysis includes:

- Interactive state-level customer charts
- Interactive city-level customer charts
- Interactive customer geographic map
- Interactive state geographic map

Users can zoom, pan, and hover over the visualizations to explore the data.

## Technologies Used

- Python
- Pandas
- NumPy
- Plotly
- Scikit-learn
- Google Colab
- GitHub

## Project Structure

```text
Week-1-Strategic-Planning/
│
├── README.md
├── week1_analysis.py
└── requirements.txt
