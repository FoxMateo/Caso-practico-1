pipeline {
    agent any

    stages {
        stage('Test Load') {
            steps {
                echo 'Ejecutando pruebas bajo sobrecarga...'
            }
            parallel {
                "Job 1": {
                    sh "sleep 30"
                },
                "Job 2": {
                    sh "sleep 30"
                },
                "Job 3": {
                    sh "sleep 30"
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completado con sobrecarga.'
        }
    }
}
