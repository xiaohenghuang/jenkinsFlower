FROM python:3.6.15-slim-buster
# frolvlad/alpine-python-machinelearning
# 

RUN pip install --upgrade pip

WORKDIR /app

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

# RUN streamlit run app.py
EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]
# CMD [ "streamlit", "run", "app.py" ]
CMD ["app.py"]
