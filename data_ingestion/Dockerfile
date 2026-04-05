FROM python:3.11-slim

# Set the working directory to the root of the project
WORKDIR /app

# Copy requirements from the root
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything into /app
COPY . .

# Force Python to look at /app for all imports
ENV PYTHONPATH=/app

CMD ["python", "-m", "uvicorn", "data_ingestion.ingestion_api:app", "--host", "0.0.0.0", "--port", "8000"]