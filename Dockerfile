FROM python:3.11-slim

WORKDIR /app

COPY tests/requiremets.txt .
RUN pip install --no-cache-dir -r requiremets.txt

COPY . .

CMD ["pytest", "tests/"]