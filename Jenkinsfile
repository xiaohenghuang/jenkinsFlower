pipeline{
    agent any
        stages{
            stage('Clone Repository'){
                steps{
                    checkout scm
                }
            }
            stage('Build Image'){
                steps{
                    sh 'sudo docker build -t mymodel:v1'
                }

            }
            stage('Run Image'){
                steps{
                    sh 'sudo docker run -d --name flowermodel mymodel:v1'
                }
            }
            stage('Test'){
                steps{
                    echo 'testing...'
                }
            }
        }
}