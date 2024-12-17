pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Descargando el código'
                git branch: 'master', 
                    credentialsId: 'github-credentials',
                    url: 'https://github.com/FoxMateo/Caso-practico-1'
            }
        }

        stage('Setup Python') {
            steps {
                echo 'Instalando dependencias del sistema...'
                sh '''
                apt-get update
                apt-get install -y python3.10-venv
                '''

                echo 'Creando entorno virtual e instalando dependencias...'
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
                echo 'Ejecutando pruebas unitarias e integración...'
                sh '''
                source venv/bin/activate
                pytest > test-results.log || true
                '''
            }
        }

        stage('Results') {
            steps {
                echo 'Archivando resultados de pruebas...'
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
