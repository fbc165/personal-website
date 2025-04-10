pipeline {
    agent any

    environment {
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
                echo "🔐 Secrets carregadas com sucesso"
            }
        }

        stage('Gerar .env') {
            steps {
                dir("${env.WORKSPACE}") {
                    sh '''
                    echo "📝 Criando .env com variáveis..."
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

        stage('Deploy com Docker Compose') {
            steps {
                dir("${env.WORKSPACE}") {
                    sh '''
                    echo "🧹 Removendo container certbot (se existir)..."
                    docker rm -f certbot || true

                    echo "🧱 Parando containers existentes..."
                    docker-compose -p $PROJECT_NAME down --remove-orphans

                    echo "🚀 Subindo nova versão..."
                    docker-compose -p $PROJECT_NAME up --build -d
                    '''
                }
            }
        }
    }
}

