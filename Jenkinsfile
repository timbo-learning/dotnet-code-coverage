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
            // Just in case something goes wrong, pipeline will be killed after a timeout
            timeout(time: 1, unit: 'HOURS') {
              // Reuse TaskId previously collected by withSonarQubeEnv
              def qg = waitForQualityGate()
              if (qg.status != 'OK') {
                error "Pipeline aborted due to quality gate failure: ${qg.status}"
              }
              //waitForQualityGate abortPipeline: true
            }
          }
        }
    }
}
