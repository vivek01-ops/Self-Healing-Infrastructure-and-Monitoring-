FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install Flask
RUN pip install flask

# Copy the webhook server code
COPY webhook-server.py /app/webhook-server.py
# COPY ../logs  # Ensure logs directory exists/

# Expose port for Flask
EXPOSE 5001

# Command to run the Flask server
CMD ["python3", "webhook-server.py"]
