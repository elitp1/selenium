# Use an official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    gnupg \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1 \
    libxss1 \
    libxtst6 \
    libx11-xcb1 \
    fonts-liberation \
    libappindicator1 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    ca-certificates \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

# Install Playwright dependencies and browsers
RUN playwright install --with-deps

# Set display env for browsers (Playwright + Selenium)
ENV DISPLAY=:99

# Default command to run tests
CMD ["pytest", "selenium_app/selenium_test.py", "--alluredir=/tmp/allure"]
