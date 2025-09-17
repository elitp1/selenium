# Start from official Playwright image (Python + browsers + system deps)
FROM mcr.microsoft.com/playwright/python:v1.55.0-jammy

# Environment settings
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DISPLAY=:99 \
    DEBIAN_FRONTEND=noninteractive

# Set working directory
WORKDIR /app

# Install Google Chrome & ChromeDriver for Selenium
RUN apt-get update && apt-get install -y wget gnupg ca-certificates && \
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-linux.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-linux.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
        > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y \
        google-chrome-stable \
        chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Default command: run Selenium/Playwright tests with Allure
CMD ["pytest", "selenium_app/selenium_test.py", "--alluredir=/tmp/allure"]