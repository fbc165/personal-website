FROM jenkins/jenkins:lts

USER root

# Instala o Docker CLI dentro do container Jenkins
RUN apt-get update && \
    apt-get install -y docker.io && \
    usermod -aG docker jenkins

USER jenkins
