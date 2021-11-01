pipeline{
    agent { dockerfile true }/*any*/
        stages{
            stage('Clone Repository'){
                steps{
                    checkout scm
                }
            }
            stage('Build Image'){
                steps{
                    sh 'docker build -t mymodel:v1'
                }

            }
            stage('Run Image'){
                steps{
                    sh 'docker run -d --name flowermodel mymodel:v1'
                }
            }
            stage('Test'){
                steps{
                    echo 'testing...'
                }
            }
        }
}