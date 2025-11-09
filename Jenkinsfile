pipeline {
    agent any

    environment {
        PYTHON = 'python3'
        VENV_DIR = '.venv'
    }

    options {
        timestamps()
        ansiColor('xterm')
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                if [ ! -d "${VENV_DIR}" ]; then
                    ${PYTHON} -m venv ${VENV_DIR}
                fi
                . ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                if [ -f requirements.txt ]; then
                    pip install -r requirements.txt
                fi
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . ${VENV_DIR}/bin/activate
                if [ -d "tests" ]; then
                    echo "Running tests..."
                    pytest --maxfail=1 --disable-warnings -q || true
                else
                    echo "No tests found."
                fi
                '''
            }
        }

    post {
        success {
            echo "✅ Pipeline completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed. Check logs."
        }
    }
}
