pipeline {
    // master executor should be set to 0
    agent any
    stages {
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
