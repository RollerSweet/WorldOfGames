# Start from a base image that has Python and pip installed
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

ENV PATH="/usr/local/bin:${PATH}"

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI project into the container
COPY . .

# Copy the Scores.txt file into the container
COPY Scores.txt /app/Scores.txt

# Set the command to run the FastAPI project
CMD ["uvicorn", "MainScores:app", "--host", "0.0.0.0", "--port", "80"]
