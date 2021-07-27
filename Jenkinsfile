pipeline {
    // master executor should be set to 0
    agent any
    stages {
        stage('checkout') {
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [[$class: 'CleanBeforeCheckout']], userRemoteConfigs: [[credentialsId: 'github_credential', url: 'https://github.com/palgoel/pytesr_allrep_jen.git']]])
            }
        }
        stage('Build Image') {
            steps {
                    bat "docker build -t palgoel/pytest_calculator ."
            }
        }
        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'pass', usernameVariable: 'user')]) {
                    //sh
			        bat "docker login --username=${user} --password=${pass}"
			        bat "docker push palgoel/pytest_calculator:latest"
			    }    

            }
		} 
    }
}
