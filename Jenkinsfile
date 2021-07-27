pipeline {
    // master executor should be set to 0
    agent any
    stages {
	    stage('checkout') {
            steps{
             checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [[$class: 'CleanBeforeCheckout']], userRemoteConfigs: [[credentialsId: 'github_credential', url: 'https://github.com/palgoel/pytesr_allrep_jen/']]])
            }
        }
        stage('Build Image') {
            steps {
				script{
               			 app = "docker build -t palgoel/pytest_calculator ."
				}
            }
        }
        stage('Push Image') {
            steps {
                    script {
						docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
			        	app.push("${BUILD_NUMBER}")
			            app.push("latest")
			        }
                }
            }
		} 
    }
}
