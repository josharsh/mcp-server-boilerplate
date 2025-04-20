FROM python:3.11-slim

WORKDIR /app

# Install uv
RUN pip install --no-cache-dir uv

# Copy requirements files
COPY requirements.txt .
COPY pyproject.toml .
COPY uv.lock .

# Install dependencies using uv with --system flag to avoid virtual environment requirement
RUN uv pip install --system --no-cache-dir -r requirements.txt
RUN uv pip install --system --no-cache-dir mcp[cli]>=1.6.0

# Copy application code
COPY main.py .
COPY app/ ./app/
COPY .env .

# Expose port for web access (if needed)
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "main.py"] 