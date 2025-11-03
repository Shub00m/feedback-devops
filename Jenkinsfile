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
                bat 'docker build -t feedback-app .'
            }
        }

        stage('Run Containers') {
            steps {
                bat 'docker run -d -p 8083:80 --name feedback-container feedback-app'
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
