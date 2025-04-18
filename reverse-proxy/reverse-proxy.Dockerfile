FROM python:3.9-slim-buster

WORKDIR /app

COPY reverse-proxy-requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY reverse_proxy.py .

# CMD 指令修改为显式指定 Flask 应用入口文件 reverse_proxy.py
CMD ["flask", "--app", "reverse_proxy.py", "run", "--host=0.0.0.0", "--port=8080"]
