pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Shub00m/feedback-devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t feedback-app -f app/Dockerfile app'
            }
        }

        stage('Run Container') {
            steps {
                bat '''
                docker stop feedback-container || echo "Already stopped"
                docker rm feedback-container || echo "Already removed"
                docker run -d -p 8083:5000 --name feedback-container feedback-app
                '''
            }
        }

        stage('Verify Container') {
            steps {
                bat 'docker ps'
                bat 'docker logs feedback-container'
            }
        }
    }
}
