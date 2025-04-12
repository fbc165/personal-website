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

     	stage('Deploy Nginx Config') {
	    steps {
	        sh 'cp -f ${WORKSPACE}/nginx/conf.d/default.conf /var/jenkins_home/shared/nginx/'
	        sh 'docker exec nginx nginx -s reload'
	    }
	}

        stage('Deploy com Docker Compose') {
            steps {
                dir("${env.WORKSPACE}") {
                    sh '''
		    ls -la
		    cat nginx/conf.d/default.conf
                    echo "🧱 Parando containers existentes..."
                    docker-compose -f docker-compose.yaml -p $PROJECT_NAME down --remove-orphans

                    echo "🚀 Subindo nova versão..."
                    docker-compose -f docker-compose.yaml -p $PROJECT_NAME up --build -d
                    '''
                }
            }
        }
    }
}

