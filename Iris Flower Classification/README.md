# Iris Flower Classification 🌸

This project uses machine learning algorithms to classify Iris flowers
into three species using their physical measurements.

## Algorithms Used
- K-Nearest Neighbors (KNN)
- Decision Tree Classifier

## Features
- Exploratory Data Analysis (EDA)
- Data Visualization
- Model Training & Evaluation
- 100% Accuracy on Test Data

## Tech Stack
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn


Kaggle Notebook: https://www.kaggle.com/code/mr1rameez/iris-flower-classification-by-knn-decision-tree

# Data Storytelling: Why These Steps Were Chosen
## 🔍 Understanding the Problem

The goal of this project is to classify Iris flowers into three species using physical measurements. Since the target variable (species) is already known, this problem naturally falls under supervised machine learning classification. The Iris dataset was chosen because it is clean, well-structured, and ideal for learning fundamental classification concepts before moving to more complex real-world datasets.

## 📊 Data Loading & Preparation

The dataset was loaded from a CSV file to simulate a real-world workflow where data is rarely pre-loaded from libraries. The Id column was removed as it does not contribute to prediction. The dataset was then split into features (X) and target (y) to clearly separate inputs from outputs, which is a best practice in machine learning pipelines.

Why this step?
Clean and well-prepared data ensures that the model learns meaningful patterns rather than noise.

## 🔎 Exploratory Data Analysis (EDA)

Before training any model, exploratory data analysis was performed using pair plots, scatter plots, box plots, and correlation heatmaps. These visualizations helped uncover relationships between features and identify which measurements contribute most to species differentiation.

Key Insight:
Petal length and petal width show strong separation between species, especially for Iris-setosa.

Why this step?
EDA helps validate whether machine learning is appropriate and provides intuition about which algorithms may perform well.

## 🤖 Model Selection

Two classification algorithms were selected:

K-Nearest Neighbors (KNN) for its simplicity and effectiveness on distance-based data

Decision Tree for its interpretability and ability to handle non-linear decision boundaries

These models were chosen because they are beginner-friendly, easy to explain, and highly effective on small, well-separated datasets like Iris.

Why these models?
They allow clear understanding of how predictions are made without complex mathematical assumptions.

## 🧪 Training & Evaluation

The dataset was split into training and testing sets to ensure unbiased evaluation. Model performance was measured using accuracy, classification reports, and confusion matrices. Both models achieved 100% accuracy, indicating perfect classification on the test data.

Why evaluate this way?
Using multiple evaluation metrics ensures that the model is not only accurate but also balanced across all classes.

## 📈 Visual Evaluation

Confusion matrices and feature importance plots were used to visually validate model performance and understand feature contributions. These visuals confirm that most classification decisions are driven by petal-related measurements.

Why visualization matters?
Visual evidence makes model behavior more transparent and easier to communicate to non-technical stakeholders.

## ✅ Conclusion

This step-by-step approach — from data understanding to visualization, modeling, and evaluation — ensures a complete and explainable machine learning workflow. The Iris dataset provides a strong foundation for understanding classification concepts, and the structured methodology used here can be applied to more complex real-world problems.

## 🚀 Final Takeaway

This project demonstrates that strong results are achieved not by complex models, but by choosing the right steps, understanding the data, and applying simple algorithms effectively.

