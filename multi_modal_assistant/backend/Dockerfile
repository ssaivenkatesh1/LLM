FROM python:3.11-slim-bookworm

# Install build tools only if needed (optional)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy only requirements first
COPY requirements.txt .

# Install dependencies (this layer gets cached)
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of your source code
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
