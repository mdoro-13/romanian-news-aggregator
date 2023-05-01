FROM python:3.9-slim

ENV NEWS_DB_NAME=<NEWS_DB_NAME> \
    NEWS_DB_USER=<NEWS_DB_USER> \
    NEWS_DB_PASSWORD=<NEWS_DB_PASSWORD> \
    NEWS_DB_HOST=<NEWS_DB_HOST> \
    NEWS_DB_PORT=<NEWS_DB_PORT>

RUN apt-get update && \
    apt-get -y install build-essential cron libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

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
