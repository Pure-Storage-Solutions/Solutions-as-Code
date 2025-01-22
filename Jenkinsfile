pipeline {
    agent any
    options {
        ansiColor('xterm')
    }
    parameters {
        choice(choices: ['terraform-infra'], description: 'Select the Solution to build', name: 'solution')
        string(name: 'count', defaultValue: "0", description: 'Number of VMs')
        choice(choices: ['fsvc', 'shared-vc'], description: 'Select the VC to use', name: 'vcenter')
        booleanParam(name: 'Build', defaultValue: false, description: 'Build Infrastructure')
        booleanParam(name: 'Install', defaultValue: false, description: 'Install and configure solution')
        booleanParam(name: 'Test', defaultValue: false, description: 'Run the performance test')
        booleanParam(name: 'Destroy', defaultValue: false, description: 'Destroy Infrastructure')
    }

    environment {
        SSH_KEY = credentials('ansible')
        WINDOWS_ADMIN_PASS = credentials('windows_admin_password')
        VC_PASS = credentials("${params.vcenter}")
        INFOBLOX_PASS = credentials('infoblox')
        AWS_ACCESS_KEY_ID = 'PSFBSAZRAECJNHNFJEKCPOHOOPMGMKMJLIJLKBCMLB'
        AWS_SECRET_ACCESS_KEY = credentials('s3token')
        ANSIBLE_HOST_KEY_CHECKING = "False"
        ANSIBLE_ROLES_PATH = "../../ansible/roles"
        vm_count = "${params.count}".toInteger()
    }

    stages {
        stage('Build Solution') {
            steps {
                script {
                    echo "Starting Build stage"
                    sol_name = params.solution
                    build_solution(sol_name)
                }
            }
        }

        stage('Install Solution') {
            when {
                expression { params.Install }
            }
            steps {
                script {
                    echo "Installing and configuring the solution"
                    sol_name = params.solution
                    install_solution(sol_name)
                }
            }
        }

        stage('Test Solution') {
            when {
                expression { params.Test }
            }
            steps {
                script {
                    echo "Running tests for the solution"
                    sol_name = params.solution
                    test_solution(sol_name)
                }
            }
        }

        stage('Destroy Solution') {
            when {
                expression { params.Destroy }
            }
            steps {
                script {
                    echo "Destroying the infrastructure"
                    sol_name = params.solution
                    destroy_solution(sol_name)
                }
            }
        }
    }
}

def build_solution(sol) {
    def tf_cmd = "/usr/bin/terraform"
    def workspace = pwd()
    def solname = sol.trim()
    def path = "${workspace}/modules/${solname}"

    dir(path) {
        if (params.Build) {
            echo "Executing Build steps for solution: ${solname}"
            sh "sed -i -e 's/sol_name/${solname}/g' backend.tf"
            sh "rm -rf .terraform"
            sh "${tf_cmd} init -upgrade"
            def count = sh(script: "grep vm_count main.tfvars | awk '{print \$3}' | xargs", returnStdout: true).trim().toInteger()
            def total_count = vm_count + count
            sh "${tf_cmd} apply -auto-approve -var-file=main.tfvars -var vsphere_password=${VC_PASS} -var ansible_key=${SSH_KEY} -var infoblox_pass=${INFOBLOX_PASS} -var vm_count=${total_count}"
            sh "python3 ../../build-inventory.py ${solname}"
        }
    }
}

def install_solution(sol) {
    sh "ansible-playbook -i hosts.ini ../../ansible/playbooks/mssql-install.yml -vvv"
}

def test_solution(sol) {
    sh "ansible-playbook -i hosts.ini ../../ansible/playbooks/mssql-test.yml -vvv"
}

def destroy_solution(sol) {
    def tf_cmd = "/usr/bin/terraform"
    def workspace = pwd()
    def solname = sol.trim()
    def path = "${workspace}/modules/${solname}"

    dir(path) {
        if (params.Destroy) {
            echo "Executing Destroy steps for solution: ${solname}"
            sh "rm -rf .terraform"
            sh "${tf_cmd} init -upgrade"
            sh "${tf_cmd} destroy -auto-approve -var-file=main.tfvars -var vsphere_password=${VC_PASS} -var ansible_key=${SSH_KEY} -var infoblox_pass=${INFOBLOX_PASS}"
        }
    }
}
