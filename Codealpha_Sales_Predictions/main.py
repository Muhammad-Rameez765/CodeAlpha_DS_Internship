from data_loader import load_and_clean_data
from eda_plots import generate_eda_plots, show_correlation
from model_training import train_sales_model

def run_pipeline():
    # 1. Load Data
    df = load_and_clean_data('Advertising.csv')

    # 2. Perform EDA
    show_correlation(df)
    generate_eda_plots(df)

    # 3. Train and Save Model
    model = train_sales_model(df)

    # 4. Final Verification
    print("\n--- Pipeline Complete ---")
    print(f"Interception: {model.intercept_}")
    print(f"Coefficients (TV, Radio): {model.coef_}")

if __name__ == "__main__":
    run_pipeline()
