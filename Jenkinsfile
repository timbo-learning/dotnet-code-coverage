pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python3 bin/build.py -k dotnet-local'
            }
        }
    }
}
