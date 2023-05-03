pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/burz3v/world_of_games.git']])
            }
        }
        stage('Build') {
            steps {
                bat 'docker-compose build'
            }
        }
        stage('Run') {
            steps {
                bat 'docker-compose up -d'
            }
        }
        stage('Test') {
            steps {
                bat 'e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                bat 'docker-compose down'
                bat 'docker-compose push'
            }
        }
    }
}
