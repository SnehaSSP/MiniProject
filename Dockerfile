# Use Python base image
FROM python:3.11-slim

# Install dependencies like Chrome and ChromeDriver
RUN apt-get update && \
    apt-get install -y curl unzip chromium chromium-driver && \
    rm -rf /var/lib/apt/lists/*

# Set environment for headless Chrome
ENV DISPLAY=:99

# Set working directory inside the container
WORKDIR /app

# Copy project files to the container
COPY . .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Command to run your test script (adjust if needed)
CMD ["pytest"]
