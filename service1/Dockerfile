# Use Python base image
FROM python:3.9-slim

# Install procps to get the 'ps' command
RUN apt-get update && apt-get install -y procps

# Set working directory
WORKDIR /app

# Copy the app code to the container
COPY . .

# Install required Python packages
RUN pip install flask
RUN pip install requests

# Expose port 8199
EXPOSE 8199

# Run the application
CMD ["python", "app.py"]
