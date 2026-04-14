FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY app ./app

# Kjører alle eksemplene i læringsrekkefølge: én qubit først, deretter to.
CMD ["sh", "-c", "python app/hello_quantum.py && python app/hello_quantum_with_two_bits.py"]
