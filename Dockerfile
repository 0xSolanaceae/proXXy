FROM python:3.12.0a7-bullseye

COPY proXXy.py /app/proXXy.py
COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python3", "proXXy.py"]
