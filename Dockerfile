From python:3.11-slim

WORKDIR /app

COPY app/requirement.txt /app/
RUN pip install --no-cache-dir -r requirement.txt

COPY app/  /app/
EXPOSE 8080
  CMD ["python", "app.py"]
