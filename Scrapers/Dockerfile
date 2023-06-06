FROM python:3.9-slim

ENV NEWS_DB_NAME=<NEWS_DB_NAME> \
    NEWS_DB_USER=<NEWS_DB_USER> \
    NEWS_DB_PASSWORD=<NEWS_DB_PASSWORD> \
    NEWS_DB_HOST=<NEWS_DB_HOST> \
    NEWS_DB_PORT=<NEWS_DB_PORT>

RUN apt-get update && \
    apt-get -y install build-essential cron libpq-dev wget curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Adding trusting keys to apt for repositories
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Adding Google Chrome to the repositories
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Updating apt to see and install Google Chrome
RUN apt-get -y update

# Magic happens
RUN apt-get install -y google-chrome-stable

# Installing Unzip
RUN apt-get install -yqq unzip

# Download the Chrome Driver
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Set display port as an environment variable
ENV DISPLAY=:99

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --user -r requirements.txt

COPY run_scrapers.sh /app/run_scrapers.sh
RUN chmod +x /app/run_scrapers.sh

COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab

RUN touch /tmp/cron.log && \
    chmod 0644 /tmp/cron.log && \
    chown root:root /tmp/cron.log && \
    crontab /etc/cron.d/crontab

CMD printenv > /etc/environment && cron && tail -f /tmp/cron.log
