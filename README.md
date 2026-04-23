# **US-Superstore-Sales-Analysis**

### Short Description:
Retail sales analysis of the Superstore dataset using Python (EDA in Jupyter Notebook) and Streamlit (dashboard). Highlights KPIs, sales trends, customer behavior, and profitability insights for portfolio presentation.

***
## 📌 Project Overview

This project analyzes the Superstore dataset (Excel file: Superstore.xlsx), a popular sample dataset for retail and sales analysis. The goal is to explore trends in sales, profit, and customer behavior using both Python (Jupyter Notebook) for in-depth analysis and Streamlit for interactive dashboard visualizations.

By combining data analysis with visualization, this project demonstrates how data-driven insights can highlight key performance indicators (KPIs), identify profitable/unprofitable product categories, and track year-over-year growth.

***

## 🗂 Files in This Project
 ### 1. Superstore.xlsx

   The raw dataset containing sales, profit, customer, and order details.
   Columns include: Order Date, Ship Date, Ship Mode, Customer Segment, Category, Sub-Category, Sales, Quantity, Discount, and Profit.


 ### 2. superstore-sales-analysis.ipynb

   A Python Jupyter Notebook containing full exploratory data analysis (EDA).
   - Covers:

     - Data cleaning and preprocessing
     - Customer segmentation and loyalty analysis
     - Sales and profit trend analysis (yearly, quarterly, monthly)
     - Product category and sub-category performance
     - Regional analysis by state and city
     - Discount vs. profitability correlation
     - Pareto analysis of customer profitability

***

 ## ⚙️ Tech Stack
   - Python (Pandas, NumPy, Matplotlib, Seaborn)
   - Jupyter Notebook
   - Streamlit (for dashboarding)
   - Excel (Superstore.xlsx dataset)

***

## 📊 Dashboard Preview
 <img width="1876" height="872" alt="image" src="https://github.com/user-attachments/assets/aeaf3466-2dca-4f70-96f3-1078c834d11d" />


***

## 📊 Key Insights

  - **Customer Concentration:** The top 30% of customers account for approximately 97% of total profit, underscoring the importance of targeted retention strategies for high-value customers.
  - **Top Segments:** The Consumer segment contributes the highest sales volume, followed by Corporate and Home Office.
  - **Shipping Preference:** Standard Class is the most frequently used shipping mode across all product categories.
  - **Regional Leaders:** California and New York rank among the top-performing states by both sales and profit.
  - **Category Performance:** Technology leads in total sales, while Office Supplies generate strong profit margins relative to their revenue.
  - **Sub-Category Profitability:** Copiers, Paper, and Accessories rank among the most profitable sub-categories despite not being top sellers in volume.
  - **Profitability Issues:** Tables rank fourth in sales but record significant losses — driven primarily by aggressive discounting rather than shipping costs.
  - **Discount Impact:** A clear negative correlation exists between discount rate and profitability across sub-categories. Tables, Machines, and Bookcases all suffer from high discounts and low-to-negative profitability.
  - **High Efficiency Cities:** Cities like Atlantic City and Grand Island show profitability ratios of 0.48–0.50, far above the dataset average of 0.125.

***

## 🚀 How to Use
  1. Open the Jupyter Notebook (superstore-sales-analysis.ipynb) to review the Python analysis.
  2. Open the dataset (Superstore.xlsx) if you want to explore or reload data.
  3. Interacting with the dashboard
   - Streamlit Public link: [https://superstore-sales-analysis-eda.streamlit.app/]
