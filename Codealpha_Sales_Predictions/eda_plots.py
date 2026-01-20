import seaborn as sns
import matplotlib.pyplot as plt

def generate_eda_plots(df):
    """Generates scatter plots for TV, Radio, and Newspaper vs Sales."""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    sns.scatterplot(data=df, x='TV', y='Sales', ax=axes[0])
    axes[0].set_title('TV vs Sales')

    sns.scatterplot(data=df, x='Radio', y='Sales', ax=axes[1])
    axes[1].set_title('Radio vs Sales')

    sns.scatterplot(data=df, x='Newspaper', y='Sales', ax=axes[2])
    axes[2].set_title('Newspaper vs Sales')

    plt.tight_layout()
    plt.savefig('eda_plots.png')
    print("EDA plots saved as eda_plots.png")
    plt.show()

def show_correlation(df):
    """Prints the correlation matrix."""
    print("\nCorrelation Matrix:")
    print(df.corr())
