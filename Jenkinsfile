pipeline {
    agent any

    environment {
        PROJECT_NAME = 'personal-django-app'
    }

    stages {
        stage('Carregar Secrets') {
            steps {
                withCredentials([
                    string(credentialsId: 'POSTGRES_DB', variable: 'POSTGRES_DB'),
                    string(credentialsId: 'POSTGRES_USER', variable: 'POSTGRES_USER'),
                    string(credentialsId: 'POSTGRES_PASSWORD', variable: 'POSTGRES_PASSWORD'),
                    string(credentialsId: 'DJANGO_SECRET_KEY', variable: 'DJANGO_SECRET_KEY'),
                    string(credentialsId: 'DEBUG', variable: 'DEBUG')
                ]) {
                    sh '''
                        echo "🔐 Criando .env com variáveis..."
                        cat > .env <<EOF
                        POSTGRES_DB=${POSTGRES_DB}
                        POSTGRES_USER=${POSTGRES_USER}
                        POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
                        DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY}
                        DEBUG=${DEBUG}
                        EOF
                    '''
                }
            }
        }
        stage('Preparar Configuração Nginx') {
            steps {
                sh '''
                    echo "📋 Preparando configuração do Nginx..."
                    mkdir -p /var/jenkins_home/shared/nginx/
                    cp -f ${WORKSPACE}/nginx/conf.d/default.conf /var/jenkins_home/shared/nginx/
                    echo "✅ Arquivo de configuração copiado com sucesso"
                '''
            }
        }

        stage('Deploy com Docker Compose') {
            steps {
                dir("${env.WORKSPACE}") {
                    sh '''
                    echo "🧱 Parando containers existentes..."
                    docker-compose -f docker-compose.yaml -p $PROJECT_NAME down --remove-orphans

                    echo "🚀 Subindo nova versão..."
                    docker-compose -f docker-compose.yaml -p $PROJECT_NAME up --build -d
                    '''
                }
            }
        }

        stage('Reload Nginx Configuration') {
            steps {
                sh '''
                    echo "🔄 Verificando se o Nginx está rodando e recarregando configuração..."
                    # Esperar um pouco para garantir que o container esteja pronto
                    sleep 5
                    
                    # Verificar se o container nginx existe e está rodando
                    if docker ps | grep -q nginx; then
                          docker cp jenkins:${WORKSPACE}/nginx/conf.d/default.conf /tmp/default.conf
                          # Copiar do host para o Nginx
                          docker cp /tmp/default.conf nginx:/etc/nginx/conf.d/default.conf
                          # Limpar arquivo temporário
                          rm /tmp/default.conf
                        echo "✅ Container Nginx encontrado, recarregando configuração..."
                        docker exec nginx nginx -t && docker exec nginx nginx -s reload
                        echo "✅ Configuração do Nginx recarregada com sucesso"
                    else
                        echo "⚠️ Container Nginx não encontrado ou não está rodando."
                    fi
                '''
            }
        }
    }
}
