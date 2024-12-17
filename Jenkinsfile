pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Descargando el código'
                git branch: 'master', 
                    credentialsId: 'github-credentials',
                    url: 'https://github.com/tu-usuario/nombre-repositorio.git'
            }
        }

        stage('Python') {
            steps {
                echo 'Instalando dependencias'
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install pytest flask
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Ejecutando pruebas unitarias'
                sh '''
                source venv/bin/activate
                pytest > test-results.log || true
                '''
            }
        }

        stage('Results') {
            steps {
                echo 'Archivando resultados de pruebas'
                archiveArtifacts artifacts: 'test-results.log', fingerprint: true
            }
        }
    }

    post {
        always {
            echo 'Pipeline completado.'
        }
    }
}
