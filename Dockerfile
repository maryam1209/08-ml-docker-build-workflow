# Use official Python 3.11 base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY data/ ./data/
COPY src/ ./src/
COPY tests/ ./tests/

# Optional: run preprocessing as a test
CMD ["python", "-c", "from src.preprocess import load_and_clean; load_and_clean('data/sample.csv')"]
