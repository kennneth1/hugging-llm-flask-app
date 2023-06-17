# Use the official Python base image
FROM python:3.9-rust

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

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