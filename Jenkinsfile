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
                    withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'pass', usernameVariable: 'user')]) {
   		                bat "docker login --username=${user} --password=${pass}"
			   	sript {
				   	app.push("${BUILD_NUMBER}")
			            	app.push("latest"
			        }
			    	
                    }	
            }
		} 
    }
}
