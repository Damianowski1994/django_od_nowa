FROM python:3.8

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install -y jq

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 8000

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD [ "python", "manage.py", "runserver"]
CMD gunicorn od_nowa.wsgi:application --log-file -
