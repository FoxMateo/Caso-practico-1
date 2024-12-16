pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/FoxMateo/Caso-practico-1'
            }
        }
        stage('Instalamos dependencias') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Ejecutamos test') {
            steps {
                script {
                    sh 'pytest --maxfail=1 --disable-warnings -q'
                }
            }
        }
    }
    post {
        always {
            junit '**/test-*.xml'
        }
    }
}
