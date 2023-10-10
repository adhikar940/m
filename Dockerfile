FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE 1  #to prevent Python from generating .pyc
ENV PYTHONUNBUFFERED 1 # disables this output buffering, which means that the output will be displayed in real-time as it is generated, without waiting for the buffer to fill up
COPY . .
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

CMD ["python","manage.py","runserver","0.0.0.0:8001"]
#docker run -d -p 8001:8001 <docker-image>
