pipeline {
    agent {
        label 'master'
    }

    stages {
        stage('Test Without Load') {
            steps {
                echo 'Ejecutando pruebas sin sobrecarga...'
                sh "sleep 10"
            }
        }
    }
    post {
        always {
            echo 'Pipeline completado sin sobrecarga.'
        }
    }
}
