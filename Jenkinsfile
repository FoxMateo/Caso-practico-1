pipeline {
    agent any

    stages {
        stage('Test Load') {
            steps {
                echo 'Ejecutando pruebas bajo sobrecarga...'
            }
        }

        stage('Parallel Test Load') {
            steps {
                script {
                    parallel(
                        "Job 1": {
                            sh "sleep 30"  // Simula tareas paralelas que sobrecargan el sistema
                        },
                    )
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
