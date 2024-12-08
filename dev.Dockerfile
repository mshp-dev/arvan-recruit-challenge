# Use the official Python base image
FROM python:3.12.8-slim-bullseye

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Expose the port on which the application will run
EXPOSE 80

# Run the Django application using gunicorn server
CMD ["gunicorn", "ip_info", "--bind", "0.0.0.0:80"]