import matplotlib.pyplot as plt
import seaborn as sns

def pair_plot(df):
    sns.pairplot(df, hue='Species')
    plt.show()

def petal_scatter(df):
    sns.scatterplot(
        data=df,
        x='PetalLengthCm',
        y='PetalWidthCm',
        hue='Species'
    )
    plt.title("Petal Length vs Petal Width")
    plt.show()

def correlation_heatmap(X):
    sns.heatmap(X.corr(), annot=True, cmap='coolwarm')
    plt.title("Feature Correlation Heatmap")
    plt.show()