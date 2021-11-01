FROM frolvlad/alpine-python-machinelearning
# python:3.6.15-slim-buster

RUN pip install --upgrade pip

WORKDIR /app

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

RUN streamlit run app.py
EXPOSE 4000
# CMD [ "streamlit", "run", "app.py" ]
