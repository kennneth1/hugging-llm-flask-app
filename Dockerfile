# Use the official Python base image
FROM python:3.8-slim
# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install system dependencies
RUN apt-get update && apt-get install -y curl build-essential

# Install Rust
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Add Rust binaries to PATH
ENV PATH="/root/.cargo/bin:${PATH}"

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . /app

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Expose the port on which the Flask application runs
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]