pipeline {
  agent any

  environment {
    // Ganti dengan nama Docker Hub kamu
    IMAGE_NAME = 'belvaaaaa/komputasiawanprojectt'
    REGISTRY = 'https://index.docker.io/v1/'
    REGISTRY_CREDENTIALS = 'dockerhub-credentials'
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          echo '🚧 Build Docker image...'
          dockerImage = docker.build("${IMAGE_NAME}:${env.BUILD_NUMBER}")
        }
      }
    }

    stage('Push Docker Image') {
      steps {
        script {
          echo '📤 Push image ke Docker Hub...'
          docker.withRegistry(REGISTRY, REGISTRY_CREDENTIALS) {
            dockerImage.push("${env.BUILD_NUMBER}")
            dockerImage.push('latest')
          }
        }
      }
    }
  }

  post {
    always {
      echo "✅ Pipeline selesai – image: ${IMAGE_NAME}:${env.BUILD_NUMBER}"
    }
  }
}
