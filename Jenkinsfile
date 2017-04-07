pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'echo "Hello"'
      }
    }
    stage('Test') {
      steps {
        sh 'echo "LOLO"'
      }
    }
    stage('Deploy') {
      steps {
        sh 'echo "Deploy"'
      }
    }
  }
  environment {
    ENV = 'TEST'
  }
}