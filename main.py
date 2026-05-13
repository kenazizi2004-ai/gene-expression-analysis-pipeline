from download import download_geo_dataset
from preprocess import extract_expression_matrix
from analysis import differential_expression
from visualize import plot_top_genes
import numpy as np

def main():
    gse = download_geo_dataset("GSE10038")

    expr = extract_expression_matrix(gse)

    # simple fake grouping (you can improve later using metadata)
    groups = np.array([0 if i % 2 == 0 else 1 for i in range(len(expr.index))])

    results = differential_expression(expr, groups)

    print(results.head())

    plot_top_genes(results)

if __name__ == "__main__":
    main()
