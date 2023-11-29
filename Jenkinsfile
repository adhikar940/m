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
                        -p 8001:8001 ${dockerImageName}
                    """

                }
            }
            }
            stage('Create Django Superuser') {
              steps {
                  script {
                      sh """
                          docker exec -it \$(docker ps -q --filter "ancestor=${dockerImageName}") \
                          python manage.py migrate
                      """
                      sh """
                          docker exec -it \$(docker ps -q --filter "ancestor=${dockerImageName}") \
                          python manage.py createsuperuser \
                          --noinput \
                          --username=${DJANGO_SUPERUSER_USERNAME} \
                          --email=${DJANGO_SUPERUSER_EMAIL} \
                          --password=${DJANGO_SUPERUSER_PASSWORD}
                      """
                  }
              }
            }


}

        }
        }
