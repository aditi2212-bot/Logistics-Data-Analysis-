import pandas as pd
import matplotlib.pyplot as plt

# Load logistics dataset
orders = pd.read_csv(
    "../data/olist_orders_dataset.csv"
)

print("Dataset Shape:", orders.shape)

print("\nDataset Columns:")
print(orders.columns)

print("\nBasic Information:")
print(orders.info())

# KPI 1: Total Orders
total_orders = orders["order_id"].nunique()

print("\nTotal Orders:", total_orders)

# KPI 2: Order Status
print("\nOrder Status:")
print(orders["order_status"].value_counts())

# Delivery Analysis


orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

orders["order_delivered_customer_date"] = pd.to_datetime(
    orders["order_delivered_customer_date"]
)

orders["delivery_days"] = (
    orders["order_delivered_customer_date"]
    - orders["order_purchase_timestamp"]
).dt.days


average_delivery = orders["delivery_days"].mean()

print(
    "\nAverage Delivery Time:",
    round(average_delivery, 2),
    "days"
)

# Basic Visualization

plt.figure(figsize=(10, 6))

orders["delivery_days"].dropna().plot(
    kind="hist",
    bins=30
)

plt.title("Distribution of Delivery Time")
plt.xlabel("Delivery Days")
plt.ylabel("Number of Orders")

plt.show()
