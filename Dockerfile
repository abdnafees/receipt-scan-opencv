FROM python:3.10

WORKDIR /receipts

RUN apt-get update -qq && apt-get install \
    'ffmpeg' \
    'libsm6'\
    'libxext6' -y
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./main.py /receipts/

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
