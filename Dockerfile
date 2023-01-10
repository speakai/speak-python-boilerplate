# start by pulling the python package
FROM python:3.9

# Copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# Switch working directory
WORKDIR /app

# Install the dependencies and packages in the requirements file
RUN pip3 install -r requirements.txt

# Copy every content from the local file to the image
COPY . /app

EXPOSE 5000

# COnfigure the container to run in an executed manner
CMD ["python", "application.py"]

