pipeline {
    environment {
      //PATH = "$PATH:bin"
      scannerHome = tool 'sonarscanner4.5'
    }
    agent any

    stages {
        stage('Build') {
            steps {
              //sonarscanner = '${scannerHome}/SonarScanner.MSBuild'
              //echo '${sonarscanner}'
              withSonarQubeEnv('sonarqube-jenkins-local') {
                // SonarScanner.MSBuild.dll is being called by this python script
                sh 'python3 bin/build.py -k dotnet-local --sonar-scanner "${scannerHome}/SonarScanner.MSBuild"'
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
