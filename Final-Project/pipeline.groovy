properties([disableConcurrentBuilds()])

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
                withEnv(["PATH+EXTRA=$PYTHON", "PATH+EXTRA=$DOCKER"]) {
                    dir ("$WORKSPACE") {
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
                withEnv(["PATH+EXTRA=$PYTHON", "PATH+EXTRA=$DOCKER"]) {
                    dir("$WORKSPACE") {
                        sh 'docker-compose down'
                    }
                }
            }
            cleanWs()
        }
    }
}