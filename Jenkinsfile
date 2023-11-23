pipeline {
    agent any
    stages {
          stage('Build Docker Image') {
            steps {
                script {
                // Get the current date and month in the format you want (e.g., DD-MM)
                    def currentDate = sh(script: 'date +%d', returnStdout: true).trim()
                    def currentMonth = sh(script: 'date +%m', returnStdout: true).trim()

                    // Set the Docker image name with date and month
                    def dockerImageName = "adhikar-django:${currentDate}-${currentMonth}"
                    // Build the Docker image
                    sh "docker build -t ${dockerImageName} ."
                }
            }
        }

        stage('Run Docker Container') {
    steps {
        script {
            sh """
                docker run -e adhikar_SECRET_KEY='_)5(4e&pr98lw+5+a_959n)f$74xdfkb603u&0ja6b^0*7grem' \
                -e adhikar_DEBUG='False' \
                -e adhikar_ALLOWED_HOSTS='*' \
                -p 8001:8001 ${dockerImageName}
            """
        }
    }
}

        }
    }
