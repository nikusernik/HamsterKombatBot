# Use a slim variant of Python that is more likely to support ARM architecture
FROM python:3.11-slim as builder
LABEL org.opencontainers.image.source=https://github.com/shamhi/HamsterKombatBot

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y gcc musl-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# Final stage
FROM python:3.11-slim

WORKDIR /app

# Copy the site-packages from the builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY . .

# Ensure the command uses the correct ARGUMENT variable
CMD ["sh", "-c", "python bot.py $${ARGUMENT:2}"]
