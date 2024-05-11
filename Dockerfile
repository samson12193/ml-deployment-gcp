# Use the official Python image as a base image
FROM python:3.12-slim

# Install development tools including GCC
RUN apt-get update && \
    apt-get install -y build-essential

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Specify the port number the container should expose
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
