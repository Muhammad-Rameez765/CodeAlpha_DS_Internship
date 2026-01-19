# Sales Prediction using Python 📈

Data: Advertising.csv
Author: Muhammad Rameez

## 📋 Project Description
This project focuses on predicting product sales based on advertising budgets spent on three different channels: TV, Radio, and Newspaper. Using Machine Learning (Linear Regression), we analyze which medium is most effective and provide a model to forecast sales for future marketing campaigns.

## 📊 Dataset Overview
The dataset contains 200 records of advertising spend (in thousands of dollars) and the resulting sales (in thousands of units).

TV: Spend on TV ads.

Radio: Spend on Radio ads.

Newspaper: Spend on Newspaper ads.

Sales (Target): The total units sold.

## 🚀 Project WorkflowData Cleaning: 

Removed redundant index columns and checked for missing values.

EDA (Exploratory Data Analysis): Visualized relationships using scatter plots and heatmaps.

Feature Selection: Identified that Newspaper had a low correlation ($0.23$) and focused on TV and Radio.

Model Building: Split data into training ($80\%$) and testing ($20\%$) sets.

Evaluation: Assessed the model using $R^2$ score and Error Metrics (MAE, RMSE).📉 

## Key Results

Accuracy: The model achieved an R-squared ($R^2$) score of 0.90, meaning it explains $90\%$ of the variance in sales.

Insights:

- Radio provides the highest relative boost in sales per unit of spend.
         
- TV is the most significant driver of total sales volume.

- Newspaper advertising was found to be statistically insignificant for this specific dataset.

