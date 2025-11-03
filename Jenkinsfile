pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Shub00m/feedback-devops.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                bat 'docker build -t feedback-app -f app/Dockerfile .'
            }
        }

        stage('Run Containers') {
            steps {
                bat 'docker-compose down || exit 0'
                bat 'docker-compose up -d'
            }
        }

        stage('Verify Containers') {
            steps {
                bat 'docker ps'
            }
        }

        stage('Clean Up') {
            steps {
                bat 'docker stop feedback-container || echo Already stopped'
                bat 'docker rm feedback-container || echo Already removed'
            }
        }
    }
}
