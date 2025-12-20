from src.data_loader import load_data
from src.eda_visualization import pair_plot, petal_scatter, correlation_heatmap
from src.model_training import split_data, train_knn, train_decision_tree
from src.model_evaluation import evaluate_model

# Load data
df, X, y = load_data("data/Iris.csv")

# Visualizations
pair_plot(df)
petal_scatter(df)
correlation_heatmap(X)

# Train-test split
X_train, X_test, y_train, y_test = split_data(X, y)

# KNN Model
print("KNN Model Results")
knn = train_knn(X_train, y_train)
evaluate_model(knn, X_test, y_test)

# Decision Tree Model
print("\nDecision Tree Results")
dt = train_decision_tree(X_train, y_train)
evaluate_model(dt, X_test, y_test)