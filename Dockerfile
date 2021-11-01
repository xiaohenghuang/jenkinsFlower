FROM python:3.6.15-slim-buster

WORKDIR /app

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

# RUN streamlit run app.py
CMD [ "streamlit", "run", "app.py" ]