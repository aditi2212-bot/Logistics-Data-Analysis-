# Week 1 - Strategic Planning and Data Exploration in Logistics

## Project Overview

This project is part of Week 1 of a Logistics Data Analysis project.

The objective is to understand how customer data can be used to support logistics planning, geographic demand analysis, and future supply chain optimization.

The project uses the Olist Brazilian E-Commerce customer dataset. The dataset contains information about customers, their geographic locations, cities, states, and ZIP-code prefixes.

The analysis focuses on understanding the geographic distribution of customers and identifying regions with high customer concentration.

---

## Objectives

The main objectives are:

- Understand the structure of the customer dataset
- Explore customer geographic distribution
- Calculate logistics-related KPIs
- Identify high-demand customer regions
- Visualize customer concentration
- Identify potential logistics planning opportunities
- Propose future clustering and optimization approaches

---

## Dataset

Dataset:

Brazilian E-Commerce Public Dataset by Olist

Dataset source:

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

The dataset used in this project is:

`olist_customers_dataset.csv`

The dataset contains customer-related information including:

- customer_id
- customer_unique_id
- customer_zip_code_prefix
- customer_city
- customer_state

---

## Logistics Scenario

The scenario considered in this project is an e-commerce company that wants to understand where its customers are geographically concentrated.

Understanding customer distribution can help logistics teams:

- Identify high-demand regions
- Plan warehouse locations
- Allocate delivery resources
- Identify important service regions
- Improve regional logistics planning
- Support future route optimization

---

## Key Performance Indicators

### 1. Total Customer Records

Measures the total number of customer records available in the dataset.

### 2. Unique Customers

Measures the number of unique customers using `customer_unique_id`.

### 3. Number of States

Measures the number of states represented in the customer dataset.

### 4. Number of Cities

Measures the number of cities represented in the dataset.

### 5. Customer Concentration by State

Measures how customers are distributed across different states.

---

## Data Science Approach

### Exploratory Data Analysis

Exploratory analysis is used to understand:

- Customer distribution by state
- Customer distribution by city
- Number of unique customers
- Geographic concentration

### Clustering

Clustering can be used in future analysis to group geographic regions according to customer concentration.

For example, regions can be grouped into:

- High customer concentration
- Medium customer concentration
- Low customer concentration

### Optimization

The geographic information can later be combined with delivery and geographic-coordinate datasets to support warehouse location planning and route optimization.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Google Colab
- GitHub

---

## Project Structure

```text
Week-1-Strategic-Planning/
│
├── README.md
├── week1_analysis.py
├── requirements.txt
└── data/
    └── README.md
