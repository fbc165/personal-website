FROM jenkins/jenkins:lts

USER root

ARG DOCKER_GID=998

# Instala o Docker CLI dentro do container Jenkins
RUN groupadd -for -g ${DOCKER_GID} docker && \
    usermod -aG docker jenkins && \
    apt-get update && \
    apt-get install -y git docker.io curl && \
    curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" \
    -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose

USER jenkins
