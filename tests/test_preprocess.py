from src.preprocess import load_and_clean

def test_load_and_clean():
    df = load_and_clean("data/sample.csv")
    
    # Dataframe should not be empty after cleaning
    assert not df.empty
    
    # No missing values should remain
    assert df.isnull().sum().sum() == 0
