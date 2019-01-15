pipeline {
    environment {
      //PATH = "$PATH:bin"
      scannerHome = tool 'sonarscanner'
    }
    agent any

    stages {
        stage('Build') {
            steps {
              withSonarQubeEnv('Sonar') {
                // SonarScanner.MSBuild.dll is being called by this python script
                sh 'python3 bin/build.py -k dotnet-local --sonar-scanner ${scannerHome}/SonarScanner.MSBuild.dll'
              }
            }
        }
        stage('Quality Gate') {
          steps {
            timeout(time: 1, unit: 'HOURS') {
              waitForQualityGate abortPipeline: true
            }
          }
        }
    }
}
