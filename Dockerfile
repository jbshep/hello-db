FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY *.py ./

ENV FLASK_APP=appserver.py
ENV FLASK_DB_PATH=/app/db

# remember that /app/db will need to be mapped to our docker volume we created
# when we 'docker run'

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]
