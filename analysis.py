import pandas as pd
import scipy.stats as stats

def differential_expression(expr, groups):
    results = []

    group_labels = list(set(groups))

    for gene in expr.columns:
        g1 = expr[gene][groups == group_labels[0]]
        g2 = expr[gene][groups == group_labels[1]]

        stat, pval = stats.ttest_ind(g1, g2, nan_policy='omit')

        results.append([gene, stat, pval])

    df = pd.DataFrame(results, columns=["Gene", "T-stat", "P-value"])
    df["Adj_P"] = df["P-value"] * len(df)

    return df.sort_values("Adj_P")
