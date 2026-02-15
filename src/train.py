from src.preprocess import load_and_clean
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def train_model():
    # Load and clean data
    df = load_and_clean("data/sample.csv")
    
    # Features and target
    X = df[["feature1", "feature2"]]
    y = df["label"]
    
    # Train logistic regression
    model = LogisticRegression()
    model.fit(X, y)
    
    # Make predictions
    preds = model.predict(X)
    
    # Print metric
    acc = accuracy_score(y, preds)
    print(f"Training completed. Accuracy: {acc:.2f}")

if __name__ == "__main__":
    train_model()
