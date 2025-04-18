FROM python:3.9-slim-buster

WORKDIR /app

COPY order-beverage-service-requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY order_beverage_service.py .

# CMD 指令修改为显式指定 Flask 应用入口文件 order_beverage_service.py
CMD ["flask", "--app", "order_beverage_service.py", "run", "--host=0.0.0.0", "--port=5000"]
