FROM selenium/standalone-chrome:latest

USER root

# Set work directory
WORKDIR /app

# Install pip and Python packages
RUN sudo apt-get update && \
    sudo apt-get install -y python3-pip && \
    pip3 install --no-cache-dir selenium webdriver-manager python-dotenv

# Copy script
COPY script.py .

# Copy environment variables
COPY .env .

CMD ["python3", "script.py"]