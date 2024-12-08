# Arvan Recruit Challenge

#### This Repository represents the steps have been taken to resolve the issues of the challenges in main part and selective part
* The main part of the challenge was as below:
  - <a href="#11-creating-vms-with-terraform">Provisioning necessary machines with terraform</a>
  - <a href="#12-spin-up-a-k8s-cluster-3-nodes-with-ansible">Deploying a kubernetes cluster with three nodes (1/one control plane, 2/two wokers) with ansible</a>
  - <a href="#13-monitoring-with-prometheusgrafana">Configure k8s cluster monitoring with Prometheus and Grafana</a>
  - <a href="#14-suitable-alerting-system">Consider implementation of a suitable alert system for the cluster</a>
  - <a href="#15-deploy-a-postgres-cluster-in-k8s">Deploy a Postgresql Cluster in k8s cluster</a>

* The selective part of the challenge was as below:
  - <a href="#write-a-web-api-with-python">Design a Web API to retrieve the country of given ip address and implement it with Go or Python</a>
  - <a href="#insert-data-into-postgres-and-query-history">Use the deployed postgresql to store data and query for history of api calls</a>
  - <a href="#deploy-workflow-into-k8s-with-cicd-and-automation">Deploy workflow into k8s with CI/CD and Automation</a>
  - <a href="#write-metrics-for-the-application-in-monitoring">Write metrics for your application</a>


## 0. Prerequisties
- #### In order to have a feature/tool reach workstation, one should at least have these tools installed and configured. 
- #### My setup was build on a Manjaro Linux and all the below tools are also available on all other platforms.
### Required cli tools 
  - aws cli
    ```bash
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    unzip awscliv2.zip
    ./aws/install
    ## confirming aws cli install
    ```
  - terraform
    ```bash
    wget -O - https://apt.releases.hashicorp.com/gpg | gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/hashicorp.list
    apt update && apt install -y terraform
    ## confirming argocd install
    terraform version
    ```
  - ansible
    ```bash
    apt install software-properties-common ca-certificates curl gnupg gpg python3-pip python3-dev
    add-apt-repository --yes --update ppa:ansible/ansible
    apt update && apt install -y ansible
    ## confirming ansible install
    ansible --version
    ```
  - kubectl
    ```bash
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
    install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
    ## confirming kubectl install
    kubectl version
    ```
  - helm cli
    ```bash
    curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
    chmod 700 get_helm.sh
    ./get_helm.sh
    ## confirming helm install
    helm version
    ```
  - argocd cli
    ```bash
    curl -sSL -o argocd-linux-amd64 https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
    install -m 555 argocd-linux-amd64 /usr/local/bin/argocd
    ## confirming argocd install
    argocd version
    ```

## 1. Main Part of the Challenge
- #### The below explanation represents the steps have been taken to resolve the issues of the main part of the challenge.
- #### All of the resources and necessary files of this part are present in <a href="https://github.com/mshp-dev/arvan-recruit-challenge/tree/main-part">main-part</a> branch of this repository.
### 1.1. Creating VMs with Terraform
- #### Here are the resources should be provisioned with terraform to have a working k8s cluster with three nodes
  * Add these provider to main.tf
    ```terraform
    terraform {
      required_providers {
        aws = {
          source  = "hashicorp/aws"
          version = "5.80.0"
        }
        tls = {
          source  = "hashicorp/tls"
          version = "4.0.6"
        }
        ansible = {
          source  = "ansible/ansible"
          version = "1.3.0"
        }
      }
    }
    ```
  * Create the VPC with aws_vpc resource
  * Create a public subnet
  * Create an internet gateway and attach it to the VPC
  * Create a route table (0.0.0.0/0 to -> IGW) and attach it to the subnet
  * Create a security group to open the required port for ssh, http and https
  * Create a security group for the control plane and a separate one for the worker nodes
  * Create a security group for flannel
  * Create three nodes with aws_instance resource inside the subnet and attach the security groups to them
    * Create a private key first
    * Create a key pair and output the private key locally
    * Create the control plane node
    * Create the worker nodes
  * Create the ansible hosts ansible_host resource
    ```bash
    ansible-galaxy collection install cloud.terraform
    ```

### 1.2. Spin up a k8s cluster (3 nodes) with Ansible
- #### The playbook.yml contains necessary tasks for setup the kubernetes cluster on newly provioned aws ec2 isntances

### 1.3. Monitoring with Prometheus+Grafana
- #### After initializing the k8s cluster in remote machines, there are some tasks in playbook.yml that installs helm chart of the Prometheus and Grafana repo in the k8s cluster.
- #### Some part of the setup process can be automated and done by ansible playbook, but to have a robust and reliable monitoring, one should customize the configurations and other stuff by hand.

### 1.4. Suitable Alerting System
- #### The prometheus alert manager could be configured with initial prometheus helm chart installation

### 1.5. Deploy a Postgres cluster in k8s
- #### After initializing the k8s cluster in remote machines, there are some tasks in playbook.yml that installs helm chart of the Postgresql Cluster repo in the k8s cluster.
- #### Retrieving postgres user password and put it in a vault or environment variables also could be done by automation in ansible playbook.

## 2. Selective Part
- #### The below explanation represents the steps have been taken to resolve the issues of the first selective part of the challenge.
- #### All of the resources and necessary files of this part are present in <a href="https://github.com/mshp-dev/arvan-recruit-challenge/tree/selective-part-1">selective-part-1</a> branch of this repository.
### 2.1. Write a Web-API with python
- #### Write a Web-API with python
  - To have a robust and concrete REST-API for this purpose, i choose python and its powerful web framework django with grate djangorestframework plugin alongside it, and also to retrieve the given ipv4 information easily, i used geocoder library from pipy.
  - The dockerfile and ci workflow for development with github action enabled for the repository on push to the selective-part-1 branch, the docker image of final application will be pushed to docker registry.
- #### Insert data into postgres and query history
  - Create a model of IPv4GeoLocationInfo to store data into database.
  - Use the deployed psotgresql with inter-cluster domain name as the main database in django
  - Insert new received ip into postgresql with django postgres engine.
  - Make sure to query already inserted data to make response to api calls faster.
- #### Deploy workflow into k8s with CI/CD and Automation
  - I created a separate branch called <a href="https://github.com/mshp-dev/arvan-recruit-challenge/tree/selective-part-1_cd">selective-part-1_cd</a> for the cd pipeline and create a helm chart for the deployment, the ci pipeline eventually will trigger the ci pipeline after successfull build.
- #### Write metrics for the application in monitoring
  - With the django app django_prometheus and prometheus_client, i added some metrics to the application.

### 2.2. Deploy an ELK cluster into k8s
- #### Gathering all error logs of application
- #### Gathering logs of all pods in k8s
- #### Visualize all logs and errors in Kibana
