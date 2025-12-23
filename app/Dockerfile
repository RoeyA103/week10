FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY ./operation/requirements.txt ./operation/
RUN pip install --no-cache-dir -r ./operation/requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]