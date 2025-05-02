FROM selenium/standalone-chrome:latest

USER root

WORKDIR /app

RUN sudo apt-get update && \
    sudo apt-get install -y python3-pip && \
    pip3 install --no-cache-dir selenium webdriver-manager python-dotenv

COPY script.py .
COPY .env .

CMD ["python3", "script.py"]