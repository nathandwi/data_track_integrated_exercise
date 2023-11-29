FROM python:3.12.0

ADD ./src/integratedexercise/ingest.py /app
ADD ./src/integratedexercise/util.py /app
ADD requirements.txt /app

RUN pip install -r requirements.txt

CMD [“python”, “./ingest.py”,"-d","2023-11-28","-e","dev"] 