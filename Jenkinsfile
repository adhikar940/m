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
                docker run -d -e adhikar_DEBUG='False' \
                -e adhikar_ALLOWED_HOSTS='*' \
                -p 8001:8001 ${dockerImageName}
            """
        }
    }
}

        }
    }
