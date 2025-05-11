
# Use Python 3.8 as a base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the necessary files into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /app/

# Set the command to run the migration tool
ENTRYPOINT ["python", "src/migrate_teams.py"]
