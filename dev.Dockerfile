# Use the official Python base image
FROM python:3.12.8-slim-bullseye

# Updating base image and installing necessary packages
# RUN apt update && \
#     apt upgrade -y && \
#     apt install -y \
#     curl \
#     gpg \
#     python3-pip \
#     python3-dev \
#     python3-pip \
apt-get clean or pip cache purge
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

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "fastapi:app", "--host", "0.0.0.0", "--port", "80"]