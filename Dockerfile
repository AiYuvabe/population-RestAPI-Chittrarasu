# Use Python 3.11 as the base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirement.txt

# Expose ports for FastAPI (8000) and Streamlit (8501)
EXPOSE 8000
EXPOSE 8501

# Start both FastAPI and Streamlit when the container runs
CMD ["sh", "-c", "uvicorn backend.main:app --host 0.0.0.0 --port 8000 & streamlit run frontend/app.py --server.port 8501 --server.address 0.0.0.0"]
