pipeline {
    agent any
    environment {
    // Get the current date and month in the format you want (e.g., DD-MM)
        def currentDate = sh(script: 'date +%d', returnStdout: true).trim()
        def currentMonth = sh(script: 'date +%m', returnStdout: true).trim()

        // Set the Docker image name with date and month
        def dockerImageName = "adhikar-django:${currentDate}-${currentMonth}"
        // From secret text
        adhikar_DEBUG = credentials('adhikar_DEBUG')
        adhikar_ALLOWED_HOSTS = credentials('adhikar_ALLOWED_HOSTS')
        DJANGO_SUPERUSER_USERNAME = "admin"
        DJANGO_SUPERUSER_EMAIL = "adhikar940@gmail.com"
        DJANGO_SUPERUSER_PASSWORD = "user1user2"
        docker_container_name = "docker_container"

    }
    stages {
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
                        -p 8002:8002 ${dockerImageName} \
                        --name ${docker_container_name}
                    """

                }
            }
            }
            stage('Create Django Superuser') {
              steps {
                  script {
                docker.exec(${docker_container_name}, "python manage.py createsuperuser --username=admin --email=admin@example.com --noinput --noinput --password ${DJANGO_SUPERUSER_PASSWORD} ")
                docker.exec(${docker_container_name}, "python manage.py changepassword admin <<< ${DJANGO_SUPERUSER_PASSWORD}")

                  }
              }
            }


}

        }
