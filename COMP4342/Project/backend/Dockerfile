# Use an official Python runtime as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install Python dependencies, including Django
RUN pip --timeout=200 install -r requirements.txt

# Copy the rest of the backend application code to the container
COPY . .

# Expose the port your Django application will run on
EXPOSE 8000

# Define the command to start your Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

CMD ["python", "manage.py", "migrate"]
