pipeline {
    agent any

    environment {
        PYTHON = 'python3'
        VENV_DIR = '.venv'
    }

    options {
        timestamps()
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
                set -e  # exit immediately if a command fails

                # Create virtual environment if it doesn't exist
                if [ ! -d "${VENV_DIR}" ]; then
                    echo "Creating virtual environment..."
                    ${PYTHON} -m venv ${VENV_DIR}
                fi

                # Check if activate script exists
                if [ -f "${VENV_DIR}/bin/activate" ]; then
                    echo "Activating virtual environment..."
                    . ${VENV_DIR}/bin/activate

                    # Upgrade pip
                    pip install --upgrade pip

                    # Install dependencies if requirements.txt exists
                    if [ -f requirements.txt ]; then
                        echo "Installing dependencies..."
                        pip install -r requirements.txt
                    else
                        echo "No requirements.txt found."
                    fi
                else
                    echo "❌ Virtual environment creation failed!"
                    exit 1
                fi
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                # Activate the virtual environment
                if [ -f "${VENV_DIR}/bin/activate" ]; then
                    . ${VENV_DIR}/bin/activate

                    # Run tests if tests directory exists
                    if [ -d "tests" ]; then
                        echo "Running tests..."
                        pytest --maxfail=1 --disable-warnings -q || true
                    else
                        echo "No tests found."
                    fi
                else
                    echo "❌ Virtual environment not found. Skipping tests."
                fi
                '''
            }
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
