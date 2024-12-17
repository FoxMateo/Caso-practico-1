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
                            sh "sleep 60"
                        },
                        "Job 2": {
                            sh "sleep 60"
                        },
                        "Job 3": {
                            sh "sleep 60"
                        },
                        "Job 4": {
                            sh "sleep 60"
                        },
                        "Job 5": {
                            sh "sleep 60"
                        },
                        "Job 6": {
                            sh "sleep 60"
                        }
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
