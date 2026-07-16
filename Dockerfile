FROM python:3.12-slim
WORKDIR /diary_app
#アプリ変更時にビルドを早くする
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["flask", "--app", "app", "run", "--host=0.0.0.0", "--port=5000", "--debug"]