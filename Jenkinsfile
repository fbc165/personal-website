pipeline {
    agent any

    environment {
        PROJECT_DIR = '/var/www/personal-website'
        PROJECT_NAME = 'personal-django-app'
    }

    stages {
        stage('Carregar Secrets') {
            environment {
                DB_NAME = credentials('POSTGRES_DB')
                DB_USER = credentials('POSTGRES_USER')
                DB_PASSWORD = credentials('POSTGRES_PASSWORD')
                DJANGO_SECRET_KEY = credentials('DJANGO_SECRET_KEY')
                DEBUG = credentials('DEBUG')
            }

            steps {
                echo "Secrets carregadas com sucesso."
            }
        }

        stage('Criar .env') {
            steps {
                dir("${PROJECT_DIR}") {
                    sh '''
                    cat > .env <<EOF
                    POSTGRES_DB=${DB_NAME}
                    POSTGRES_USER=${DB_USER}
                    POSTGRES_PASSWORD=${DB_PASSWORD}
                    DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY}
                    DEBUG=${DEBUG}
                    EOF
                    '''
                }
            }
        }

        stage('Atualizar Código') {
            steps {
                dir("${PROJECT_DIR}") {
                    sh 'git pull origin main'
                }
            }
        }

        stage('Deploy com Docker Compose') {
            steps {
                dir("${PROJECT_DIR}") {
                    sh '''
                    docker-compose -p $PROJECT_NAME down
                    docker-compose -p $PROJECT_NAME up --build -d
                    '''
                }
            }
        }
    }
}
