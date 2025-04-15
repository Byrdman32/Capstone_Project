# Use the base image from your devcontainer.json
FROM mcr.microsoft.com/devcontainers/base:bullseye

# Install pip package manager
RUN apt-get update && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies with pip
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Install Node.js and npm package manager
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Install front-end dependencies with npm
WORKDIR /workspace/frontend
COPY frontend/package.json ./
RUN npm install
WORKDIR /workspace

EXPOSE 9000

# Set the working directory
WORKDIR /workspace