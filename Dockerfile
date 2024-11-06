# the official Python image from Docker Hub
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
#COPY requirements.txt /app/

# Install the required dependencies from requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt


# Copy the local code and data files to the container's working directory
COPY app.py /app/
COPY rent_house_data.xlsx /app/

# Install necessary Python libraries
RUN pip install --no-cache-dir pandas scikit-learn openpyxl

# Run the Python script when the container starts
#CMD ["python", "app.py"] && tail -f /dev/null

CMD ["sh", "-c", "python app.py && tail -f /dev/null"]
