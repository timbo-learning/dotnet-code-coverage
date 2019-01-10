pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python bin/build.py -k dotnet-local'
            }
        }
    }
}
