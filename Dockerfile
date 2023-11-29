FROM python:3.12.0

ADD ./src/integratedexercise/ingest.py .
ADD ./src/integratedexercise/util.py .
ADD requirements.txt .

RUN pip install -r requirements.txt

CMD [“python”, “ingest.py”,"-d","2023-11-28","-e","dev"] 