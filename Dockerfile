# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install Rust dependencies
RUN apt-get update && apt-get install -y curl build-essential
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Add Rust binaries to PATH
ENV PATH="/root/.cargo/bin:${PATH}"

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . /app

# Set the environment variable for Flask
ENV FLASK_APP=main.py

# Expose the port on which the Flask application runs
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]