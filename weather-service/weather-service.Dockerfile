FROM python:3.9-slim-buster

WORKDIR /app

COPY weather-service-requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY weather_service.py .

CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
