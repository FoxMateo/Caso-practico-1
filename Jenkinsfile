pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/FoxMateo/Caso-practico-1'
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    sh 'pytest --maxfail=5 --disable-warnings -q'
                }
            }
        }
    }
}