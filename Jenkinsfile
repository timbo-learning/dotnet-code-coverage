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
                sh 'python3 bin/build.py -k dotnet-local --sonar-scanner "${scannerHome}/SonarScanner.MSBuild" \
                                         -d sonar.cs.opencover.reportsPaths=calculation.opencover.xml,prime.opencover.xml \
                                            sonar.dotnet.visualstudio.solution.file=unit-testing-using-dotnet-test.sln'

              }
            }
        }
        stage('Quality Gate') {
          steps {
            // Just in case something goes wrong, pipeline will be killed after a timeout
            timeout(time: 5, unit: 'MINUTES') {
              //waitForQualityGate abortPipeline: true
            }
          }
        }
    }
}
