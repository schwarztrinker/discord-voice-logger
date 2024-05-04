# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the source code from your host to your image filesystem.
COPY ./bot.py .

# Run bot.py when the container launches
CMD ["python3", "bot.py"]