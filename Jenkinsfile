pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
                
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    venv/bin/python -m pip install --upgrade pip
                    venv/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    venv/bin/python -m pytest -v \
                        --junitxml=test-results.xml
                '''
            }
        }
    }

    post {

        always {
            junit(
                testResults: 'test-results.xml',
                allowEmptyResults: true
            )
        }

        success {
            echo 'All tests passed successfully!'
        }

        failure {
            echo 'Some tests failed.'
        }
    }
}