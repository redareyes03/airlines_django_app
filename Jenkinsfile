pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_VERSION = '1.29.2'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Test') {
            steps {
                sh '''
                    docker-compose run web python ./manage.py test
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker-compose down
                    docker-compose up -d
                '''
            }
        }
    }

    post {
        always {
            sh 'docker-compose logs'
        }
        failure {
            echo 'Pipeline failed!'
        }
        success {
            echo 'Pipeline succeeded!'
        }
    }
}