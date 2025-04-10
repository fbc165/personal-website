FROM jenkins/jenkins:lts

USER root

# Instala o Docker CLI dentro do container Jenkins
RUN apt-get update && \
    apt-get install -y docker.io curl && \
    curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" \
    -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose && \
    usermod -aG docker jenkins

USER jenkins
