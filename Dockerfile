# Use an official Python runtime as a parent image
FROM python:3.9
 
# Set the working directory to /app
WORKDIR /app

# Copy the rest of the application code to the container
COPY . /app/
 
# Install the required dependencies
RUN pip install --upgrade pip
RUN pip install -e .
 
 
# Expose the port on which FastAPI will run
EXPOSE 7000
 
# Define the command to start the FastAPI application
CMD ["python", "/app/main.py"]