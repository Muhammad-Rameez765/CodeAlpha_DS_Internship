from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import joblib

def train_sales_model(df):
    """Trains a Linear Regression model on TV and Radio features."""
    # Feature selection based on EDA (Removing Newspaper)
    X = df[['TV', 'Radio']]
    y = df['Sales']

    # 80/20 Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions and Evaluation
    predictions = model.predict(X_test)
    r2 = metrics.r2_score(y_test, predictions)
    mae = metrics.mean_absolute_error(y_test, predictions)

    print(f"Model Trained. R2 Score: {r2:.4f}, MAE: {mae:.4f}")
    
    # Save the model
    joblib.dump(model, 'sales_prediction_model.pkl')
    return model

if __name__ == "__main__":
    print("Module for training the model.")
