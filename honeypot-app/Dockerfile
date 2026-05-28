FROM python:3.11-alpine
WORKDIR /app
COPY honeypot.py .
RUN adduser -D -u 10001 honeypotuser
USER honeypotuser
EXPOSE 6379
CMD ["python", "-u", "honeypot.py"]
