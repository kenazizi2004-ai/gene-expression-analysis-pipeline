import seaborn as sns
import matplotlib.pyplot as plt

def plot_top_genes(df, n=10):
    top = df.nsmallest(n, "Adj_P")

    plt.figure(figsize=(10,5))
    sns.barplot(data=top, x="Gene", y="Adj_P")
    plt.xticks(rotation=45)
    plt.title("Top Differentially Expressed Genes")
    plt.show()
