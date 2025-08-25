# Stage 1: Postgress 

#FROM postgres:15 AS postgres

# Set up PostgreSQL database
#ENV POSTGRES_USER=django_user
#ENV POSTGRES_PASSWORD=password
#ENV POSTGRES_DB=django_db

# Use the official pgAdmin image as the base
#FROM dpage/pgadmin4:latest

# Set default environment variables for pgAdmin
#ENV PGADMIN_DEFAULT_EMAIL=admin@example.com 
#ENV PGADMIN_DEFAULT_PASSWORD=admin 
#ENV PGADMIN_CONFIG_SERVER_MODE=True

# (Optional) Add any additional configuration or files
#COPY custom_config.py /pgadmin4/config_distro.py





# Stage 2: Django
FROM python:3.12

# Prevent Python from generating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY ./requirements.txt .

# no-cache-dir keeps the final image smaller, as no cached files will be stored in the image layers.
RUN pip install --no-cache-dir -r requirements.txt  

# Copy application code
COPY . .

# Set the environment file for Docker
ENV ENV_FILE=.dev_env

RUN python manage.py collectstatic --noinput
#RUN python manage.py migrate

#CMD ["python", "manage.py", "runserver", "0.0.0.0:9001"]
CMD gunicorn m.wsgi:application --bind 0.0.0.0:9001 --workers 3

# Expose ports
EXPOSE 9001


# Set working directory
#WORKDIR /app

# Copy application code from Build Stage
#COPY --from=builder /app /app

# Collect static files in final image
#RUN python manage.py collectstatic --noinput

#CMD ["bash", "-c", "service postgresql start && python manage.py runserver 0.0.0.0:8000"]

