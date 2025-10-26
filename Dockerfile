# Use Python 3.11 slim image for smaller size and better performance
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Set work directory
WORKDIR /app

# Install system dependencies required for scientific computing
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    gfortran \
    libopenblas-dev \
    liblapack-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash qfinbox

# Copy requirements first for better Docker layer caching
COPY requirements-prod.txt .

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip setuptools wheel && \
    pip install -r requirements-prod.txt

# Copy project files
COPY . .

# Install the package in development mode
RUN pip install -e .

# Change ownership to non-root user
RUN chown -R qfinbox:qfinbox /app

# Switch to non-root user
USER qfinbox

# Expose port for Jupyter notebooks or web applications
EXPOSE 8888

# Default command - can be overridden
CMD ["python", "-c", "import qfinbox; print('qfinbox is ready!')"]
