pipeline {
    agent any

    environment {
        IMAGE_TAG = "${env.BUILD_NUMBER}"
        DOCKER = '"C:\\Users\\Appex\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe"'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Images') {
            steps {
                bat '%DOCKER% build -t course-service:%IMAGE_TAG% ./course-service'
                bat '%DOCKER% build -t student-service:%IMAGE_TAG% ./student-service'
            }
        }

        stage('Deploy (Compose)') {
            steps {
                bat '%DOCKER% compose down'
                bat '%DOCKER% compose up -d --build'
            }
        }
    }

    post {
        success { echo 'Pipeline completed successfully.' }
        failure { echo 'Pipeline failed — check stage logs above.' }
    }
}