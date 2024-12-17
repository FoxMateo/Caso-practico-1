pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Descargando el código fuente...'
                git branch: 'master',
                    credentialsId: 'github-credentials',
                    url: 'https://github.com/FoxMateo/Caso-practico-1'
            }
        }

        stage('Setup Python') {
            steps {
                echo 'Instalando dependencias...'
                sh '''
                apt-get update
                apt-get install -y python3.10-venv
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Ejecutando pruebas unitarias...'
                sh '''
                . venv/bin/activate
                export PYTHONPATH=$PYTHONPATH:$WORKSPACE
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
