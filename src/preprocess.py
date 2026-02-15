
def load_and_clean(file_path):
    """
    Load CSV and drop rows with missing values.
    """
    df = pd.read_csv(file_path)
    df_clean = df.dropna()
    return df_clean
