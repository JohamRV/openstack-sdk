# Use the official Python 3.11 image as the base
FROM python:3.11

# Set the working directory inside the container
WORKDIR /openstack-sdk

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install pip dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose any necessary ports
EXPOSE 8000

# Set the command to run the application
CMD ["uvicorn", "src.main:app"]