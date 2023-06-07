FROM python:3.7-alpine
ENV DATA_DIR=data
WORKDIR /new
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "./app.py"]
CMD ["python", "./get_results.py"]