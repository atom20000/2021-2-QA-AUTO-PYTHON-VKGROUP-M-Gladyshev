
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
                //sh "docker network inspect $NETWORK >/dev/null"
                sh "docker network create $NETWORK"
                echo 'build done!'
            }
        }

        stage("Start system and tests") {
            steps {
                withEnv(["NETWORK=$NETWORK"]) {
                    dir ("Final-Project") {
                        sh "docker-compose up --abort-on-container-exit"
                    }
                }
            }
        }
    }

    post {
        always {
            allure([
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'alluredir']]
            ])
            script {
                withEnv(["NETWORK=$NETWORK"]) {
                    dir("Final-Project") {
                        sh 'docker-compose down'
                    }
                }
            }
            cleanWs()
        }
    }
}