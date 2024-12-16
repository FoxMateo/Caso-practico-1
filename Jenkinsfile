pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/FoxMateo/Caso-practico-1'
            }
        }
        stage('Instalamos dependencias') {
            steps {
                bat 'echo Installing dependencies'
            }
        }
        stage('Ejecutamos test') {
            steps {
                bat 'echo Running tests'
                // Asegúrate de ejecutar las pruebas aquí.
            }
        }
    }
    post {
        always {
            junit '**/path-to-test-reports/*.xml' // Ajusta esta ruta
        }
    }
}
