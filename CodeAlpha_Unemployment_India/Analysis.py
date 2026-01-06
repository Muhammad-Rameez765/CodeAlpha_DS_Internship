import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Configuration
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)
    # Standardizing column names (removing extra spaces)
    df.columns = df.columns.str.strip()
    
    # Date conversion with error handling
    df['Date_obj'] = pd.to_datetime(df['Date'], format='%d-%m-%Y', errors='coerce')
    
    # Dropping rows where Date conversion failed or data is missing
    df = df.dropna(subset=['Date_obj', 'Estimated Unemployment Rate (%)'])
    return df

def generate_visualizations(df):
    # 1. National Trend Analysis
    monthly_unemployment = df.groupby('Date_obj')['Estimated Unemployment Rate (%)'].mean()
    
    plt.figure(figsize=(12, 6))
    plt.plot(monthly_unemployment.index, monthly_unemployment.values, marker='o', color='tab:red')
    
    # Annotating COVID-19 Lockdown
    plt.axvline(pd.Timestamp('2020-03-01'), linestyle='--', color='black', alpha=0.7)
    plt.text(pd.Timestamp('2020-03-15'), 22, 'Lockdown Start', fontsize=12, color='red')
    
    plt.title("Impact of COVID-19 on India's Unemployment Rate")
    plt.xlabel("Timeline")
    plt.ylabel("Unemployment Rate (%)")
    plt.grid(True)
    plt.savefig('unemployment_trend.png')
    print("Graph saved as unemployment_trend.png")

if __name__ == "__main__":
    # Replace with your actual file name
    data_file = 'Unemployment_Rate_upto_11_2020.csv'
    
    try:
        data = load_and_clean_data(data_file)
        print("Data loaded successfully!")
        
        # Display colorful summary for the console
        print("\n--- Data Summary Statistics ---")
        print(data.describe())
        
        generate_visualizations(data)
        
    except FileNotFoundError:
        print(f"Error: {data_file} not found. Please ensure the dataset is in the folder.")
