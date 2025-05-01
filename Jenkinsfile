pipeline {
    agent any
    environment {
    // Get the current date and month in the format you want (e.g., DD-MM)
        def currentDate = sh(script: 'date +%d', returnStdout: true).trim()
        def currentMonth = sh(script: 'date +%m', returnStdout: true).trim()
        def currentTime = sh(script: 'date +%H%M%S', returnStdout: true).trim()
        // Set the Docker image name with date and month
        def dockerImageName = "adhikar-django:${currentDate}-${currentMonth}"
        // From secret text
        adhikar_DEBUG = credentials('adhikar_DEBUG')
        adhikar_ALLOWED_HOSTS = credentials('adhikar_ALLOWED_HOSTS')
        DJANGO_SUPERUSER_USERNAME = "admin10"
        DJANGO_SUPERUSER_EMAIL = "adhikar940@gmail1.com"
        DJANGO_SUPERUSER_PASSWORD = "user1user2"
        docker_container_name = "django_container-${currentDate}-${currentMonth}-${currentTime}"
        DJANGO_PORT = 9001

    }
    stages {
    stage('Port check and Terminate') {
            steps {
                script {
                    // Check if port 8001 is in use
                    def isPortInUse = sh(script: "lsof -i :${DJANGO_PORT}", returnStatus: true) == 0

                    if (isPortInUse) {
                        echo "Port ${DJANGO_PORT} is in use."

                        // Find and terminate processes using port 8001
                        sh "lsof -ti :${DJANGO_PORT} | xargs kill -9"

                        echo "Processes using port ${DJANGO_PORT} terminated."
                    } else {
                        echo "Port ${DJANGO_PORT} is not in use."
                    }
                }
                }
                }
          stage('Build Docker Image') {
            steps {
                script {

                    sh "docker build -t ${dockerImageName} ."
                }
            }
        }
          stage('Run Docker Container') {
            steps {
                script {
                    sh """
                        echo "dockerImageName: ${dockerImageName}"
                        docker run -d -e adhikar_DEBUG=${adhikar_DEBUG} \
                        -e adhikar_ALLOWED_HOSTS=${adhikar_ALLOWED_HOSTS} \
                        -p ${DJANGO_PORT}:${DJANGO_PORT}  \
                        --name ${docker_container_name} ${dockerImageName}

                    """

                }
            }
            }
            stage('Create Django Superuser') {
              steps {
                  script {
                  sh "docker exec -t ${docker_container_name} bash -c 'DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD} python manage.py createsuperuser --username ${DJANGO_SUPERUSER_USERNAME} --email ${DJANGO_SUPERUSER_EMAIL} --noinput'"

                  }
              }
            }
}

        }
