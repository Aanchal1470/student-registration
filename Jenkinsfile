
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Maven Build') {
            steps {
                bat '"C:\\Users\\aanchal mishra\\Downloads\\apache-maven-3.10.0-bin\\apache-maven-3.10.0\\bin\\mvn.cmd" clean package'
            }
        }
    }

    post {
        success {
            echo 'Student Registration Build Successful!'
        }
        failure {
            echo 'Build Failed!'
        }
    }
}
