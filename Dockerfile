
FROM python:3.9-slim
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir paho-mqtt
CMD ["python", "./main.py"]