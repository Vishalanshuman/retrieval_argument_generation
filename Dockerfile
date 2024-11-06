# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies
RUN pip install  -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port your app runs on
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
