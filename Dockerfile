FROM tensorflow/tensorflow:latest

RUN apt-get update && apt-get install -y libgl1-mesa-glx

WORKDIR /workdir

ADD ./requirements.txt /workdir

RUN pip install --no-cache-dir -r requirements.txt

ADD . /workdir

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]