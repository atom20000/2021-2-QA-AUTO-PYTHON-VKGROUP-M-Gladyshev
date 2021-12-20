
pipeline {
    agent {
        label 'master'
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '3'))
        timestamps()
    }

    environment {
        NETWORK = "nework${BUILD_NUMBER}"
    }

    stages {

        stage("Create docker-compose network") {
            steps {
                echo 'Start'
                sh "docker network inspect $NETWORK >/dev/null"
                sh "docker network create $NETWORK"
                echo 'Network created'
            }
        }

        stage("Start system and tests") {
            steps {
                try{
                    withEnv(["NETWORK=$NETWORK"]) {
                        dir ("Final-Project") {
                            sh "docker-compose up "
                        }
                    }
                } catch(Exception e){
                    error "Stage interrupted with ${e.toString()}"
                    sh "exit 1"
                }
                
            }
        }

        stage("Remove nemwork and stop docker-compose"){
            steps {
                withEnv(["NETWORK=$NETWORK"]) {
                    dir("Final-Project") {
                        sh 'docker-compose down -v'
                        sh "docker network rm $NETWORK"
                    }
                }
            }
        }

        stage("Allure"){
            steps{
                script{
                    allure([
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: '$WORKSPACE/alluredir']]
                    ])
                }
            }
        }
    }

    post {
        always {
            cleanWs() 
        }
    }
}