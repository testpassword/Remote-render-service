// Kulbako Artemy 2020 for Luxoft

pipeline {
    agent none
    parameters {
        string(name: 'INPUT_FILE', description: 'Absolute path to file', trim: true)
        string(name: 'WIDTH', defaultValue: '1280', description: 'Resolution by X of result image', trim: true)
        string(name: 'HEIGHT', defaultValue: '720', description: 'Resolution by Y of result image', trim: true)
        choice(name: 'FORMAT', choices: ['JPEG', 'PNG', 'BMP'], description: 'File format for render')
        string(name: 'COMPRESSION', defaultValue: '0', description: 'Compression ratio: 0 = no compression, 100 = max', trim: true)
        choice(name: 'ANTIALIASING_ALGORITHM', choices: ['OFF', 'FXAA', 'SSAA 5x', 'SSAA 8x', 'SSAA 11x', 'SSAA 16x', 'SSAA 32x'])
    }
    stages {
        stage('Prepare') {
            agent any
            steps {
                script {
                    def inputFile = new File("$INPUT_FILE") //this trick allow us to download file anywhere from fs
                    def fileName = inputFile.getName()
                    def fileFolder = inputFile.getParent()
                    dir(fileFolder) {
                        stash allowEmpty: false, includes: fileName, name: 'scene'
                    }
                }
            }
        }
        stage('Render') {
            agent { label 'gpu' }
            steps {
                unstash "scene"
                script {
                    def command = "python ${env.bps} " +
                            "--input $INPUT_FILE " +
                            "--output ${env.WORKSPACE}/ " +
                            "--width $WIDTH " +
                            "--height $HEIGHT " +
                            "--format $FORMAT " +
                            "--compress $COMPRESSION " +
                            "--aa $ANTIALIASING_ALGORITHM"
                    if (isUnix()) sh """$command"""
                    else bat """$command"""
                }
            }
            post {
                success {
                    archiveArtifacts artifacts: 'image*', fingerprint: true
                    archiveArtifacts artifacts: 'log*', fingerprint: true
                }
                cleanup {
                    cleanWs()
                }
            }
        }
    }
}