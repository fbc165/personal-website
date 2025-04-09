pipeline {
    agent any

    environment {
        IMAGE_NAME = 'personal-website:latest'
        CONTAINER_NAME = 'personal-website'
    }

    stages {
        stage('Clonar Repositório') {
            steps {
                git branch: 'main', url: 'https://github.com/fbc165/personal-website.git'
            }
        }

        stage('Build da Imagem Docker') {
            steps {
                sh "docker build -t $IMAGE_NAME ."
            }
        }

        stage('Deploy Container') {
            steps {
                // Remove container antigo, se existir
                sh """
                docker rm -f $CONTAINER_NAME || true
                docker run -d --name $CONTAINER_NAME -p 80:80 $IMAGE_NAME
                """
            }
        }
    }
}
