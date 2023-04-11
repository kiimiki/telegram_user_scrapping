# Use the Python 3.8 image as the base
FROM python:3.8

# Set the working directory
WORKDIR /app

# Copy the script and requirements file to the working directory
COPY script.py .
COPY requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

# Expose any necessary ports
EXPOSE 80

# Set the command to run the script when the container starts
CMD ["python", "script.py"]
