FROM python:3.12-slim

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Use gunicorn for production-style server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
