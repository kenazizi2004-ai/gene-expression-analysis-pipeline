import numpy as np

def extract_expression_matrix(gse):
    df = gse.pivot_samples('VALUE')
    
    df = df.dropna(axis=1, how='any')
    
    # log normalization
    df = np.log2(df + 1)
    
    return df
