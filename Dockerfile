# Multi-stage Dockerfile for space CLI application
# Stage 1: Builder - Install dependencies
FROM python:3.11-slim as builder

# Set working directory
WORKDIR /app

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files
COPY requirements.txt pyproject.toml ./
COPY src/ ./src/

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir .

# Stage 2: Runtime - Minimal image for running the application
FROM python:3.11-slim

# Set metadata
LABEL maintainer="Victor Velasquez <victorcop90@gmail.com>"
LABEL description="CLI application to fetch and display astronauts currently in space"
LABEL version="0.1.0"

# Create non-root user for security
RUN useradd -m -u 1000 spaceuser && \
    mkdir -p /app && \
    chown -R spaceuser:spaceuser /app

# Set working directory
WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin/space /usr/local/bin/space

# Copy application code
COPY --chown=spaceuser:spaceuser src/ ./src/
COPY --chown=spaceuser:spaceuser .env.example .env

# Switch to non-root user
USER spaceuser

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Health check (optional - useful for service deployments)
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD space --version || exit 1

# Default command
ENTRYPOINT ["space"]
CMD []
