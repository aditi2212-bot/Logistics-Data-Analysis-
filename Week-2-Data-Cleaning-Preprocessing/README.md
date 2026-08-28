# Week 2 - Data Collection, Cleaning and Preprocessing for Logistics Analysis

## Project Overview

This project focuses on data collection, data quality assessment, cleaning, and preprocessing for logistics analysis.

The project uses customer and geographic data from the Olist Brazilian E-Commerce Public Dataset.

The objective is to prepare reliable and structured data that can be used for future logistics analytics, geographic analysis, customer segmentation, and machine learning.

The preprocessing pipeline focuses on identifying missing values, duplicate records, invalid values, inconsistent categorical data, and numerical scaling requirements.

## Objectives

The main objectives are:

- Collect and inspect logistics-related customer data
- Understand the structure and characteristics of the dataset
- Identify missing values
- Detect duplicate records
- Identify invalid ZIP-code values
- Standardize city and state information
- Validate geographic information
- Encode categorical variables
- Normalize numerical features
- Generate a clean dataset for future analysis

## Dataset

The project uses:

- `olist_customers_dataset.csv`
- `olist_geolocation_dataset.csv`

The customer dataset contains:

- customer_id
- customer_unique_id
- customer_zip_code_prefix
- customer_city
- customer_state

The geolocation dataset contains:

- geolocation_zip_code_prefix
- geolocation_lat
- geolocation_lng
- geolocation_city
- geolocation_state

## Dataset Source

Olist Brazilian E-Commerce Public Dataset:

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

The raw datasets are not included in this GitHub repository.

## Data Quality Problems

The project checks for the following data quality issues:

### Missing Values

Missing values are identified using Pandas.

Categorical missing values are replaced with `Unknown`.

Numerical missing values are handled using median imputation where appropriate.

### Duplicate Records

Exact duplicate rows are identified and removed.

Customer IDs are also checked for duplicate values.

Repeated `customer_unique_id` values are not automatically removed because the same customer can be associated with multiple customer records.

### Invalid ZIP Codes

ZIP-code prefixes are converted to numeric values and checked for invalid values.

### Inconsistent Text

City and state values are cleaned by:

- Removing leading and trailing spaces
- Standardizing city names to lowercase
- Standardizing state codes to uppercase

### Categorical Variables

State information is converted into numerical features using one-hot encoding.

### Numerical Scaling

ZIP-code information is standardized using `StandardScaler` when required for machine learning applications.

## Preprocessing Pipeline

The preprocessing workflow is:

```text
Data Collection
       ↓
Data Inspection
       ↓
Missing Value Detection
       ↓
Duplicate Detection
       ↓
Data Validation
       ↓
Text Standardization
       ↓
ZIP Code Validation
       ↓
Feature Engineering
       ↓
Categorical Encoding
       ↓
Numerical Scaling
       ↓
Clean Dataset
