# Use the official Python 3.7 image as a base
FROM python:3.7-bullseye
LABEL authors="debjyotisarkar"

RUN apt-get update && \
    apt-get install -y curl openjdk-11-jdk procps &&\
     apt-get clean

# Verify java path
RUN update-alternatives --set java /usr/lib/jvm/java-11-openjdk-arm64/bin/java

# Set JAVA_HOME environment variable
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-arm64

# Install Spark
ENV SPARK_VERSION=3.3.1
RUN curl -o spark.tgz "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop3.tgz" && \
    tar xzf spark.tgz -C /opt/ && \
    rm spark.tgz

# Set SPARK_HOME environment variable
ENV SPARK_HOME=/opt/spark-${SPARK_VERSION}-bin-hadoop3

# Add Spark to PATH
ENV PATH=$SPARK_HOME/bin:$PATH

# Install PySpark
RUN pip install pyspark==${SPARK_VERSION} faker

# Copy the application code into the container
COPY . /app

#RUN chmod +x entrypoint.sh
# Set the working directory to /app
WORKDIR /app


# Command to run your PySpark application
# Replace 'your_script.py' with your actual script name
CMD spark-submit --name anonymize_job --py-files app.zip driver.py
