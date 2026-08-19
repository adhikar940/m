# Adhikar

Welcome to the project!  
This repository contains detailed documentation organized inside the `/readme` folder.

## 📚 Documentation Sections

| Topic | Description |
|-------|-------------|
| [Requirements](readme/requirements.md) | Info related to requirements |
| [Changelog](changelog.md) | Detailed record of changes across versions |
| [GIS & Boundaries](readme/gis.md) | Spatial data, shapefiles, and postgis documentation |
| [Database Documentation](docs/db_readme.md) | Database structure and backup instructions |

Click any link above to open the corresponding document.






Apps :

area_pop : This app is for creating all kind of areas like state, district, city, etc

Docker data :

docker build -t <docker_image> .   ### for creating docker image
docker build -f <docker_file_name> -t <image_name>:<tag> . ### for custom docker file

docker run -e adhikar_DEBUG='False' -e adhikar_ALLOWED_HOSTS='*' -p 8000:8000 -p 80:80 -p 443:443 -p 5432:5432 -p 5050:5050 --name <docker_container> <docker_image> python manage.py runserver 0.0.0.0:8000 ### for running docker image.   ### for running docker

docker run -e adhikar_DEBUG='False' -e adhikar_ALLOWED_HOSTS='*' -p 9001:9001 -p 80:80 -p 443:443 -p 5432:5432 -p 5050:5050 --name test_con test

docker run -p <host_port1>:<container_port1>

docker compose up ### for running docker-compose.yml

docker build -t test . 

docker tag local-image:tagname <dockerhub_repo_name>:tagname
docker push <dockerhub_repo_name>:tagname


- [Database](./docs/db_readme.md)