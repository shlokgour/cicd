pipeline {
    agent any

    environment {
        IMAGE_TAG = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Images') {
            steps {
                bat 'docker build -t course-service:%IMAGE_TAG% ./course-service'
                bat 'docker build -t student-service:%IMAGE_TAG% ./student-service'
            }
        }

        stage('Deploy (Compose)') {
            steps {
                bat 'docker compose down'
                bat 'docker compose up -d --build'
            }
        }
    }

    post {
        success { echo 'Pipeline completed successfully.' }
        failure { echo 'Pipeline failed — check stage logs above.' }
    }
}