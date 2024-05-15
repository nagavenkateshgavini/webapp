# User authentication webapp with GCP
Cloud native web application

Terraform Repo: https://github.com/nagavenkateshgavini/tf-gcp-infra
Cloud Function Repo: https://github.com/nagavenkateshgavini/serverless

## Run details
1. activate env
    - with Conda: ```conda activate venv```
    - with virtualenv
      ```
      python -m venv env
      source env/bin/activate
      ```
2. Install requirements    
```commandline
pip install -r requirements.txt
```
3. Run the app
   ```commandline
   export FLASK_APP=app
   flask run
   ```

## This repository can act as tutorial or example project for following concepts
  - Github workflow actions for python application to set up CI/CD
  - flask application with blueprints and sqlalchemy to organise projects in a better way
  - back end python application with flask
  - flask application with CRUD operations
  - Exception handling with custom error message and status codes in python flask app
  - Integrations tests with pytest framework, tests the integration between mysql and flask API server
  - Google cloud golden Image creation with packer when new PR gets merged
  - Developed a RESTful API with multiple endpoints like /healthz, /v1/user for health checks and user management using Node.js and Sequelize.
  - Conducted integration testing for all API endpoints with pytest.
  - Created a custom compute engine image with Hashicorp Packer and managed the service startup using systemd.
  - Configured VPCs, subnets, compute engine, CloudSQL, and set up VPC peering through Private services access.
  - Set up Cloud DNS with an A record for my domain pointing to the compute engine IP.
  - Installed Ops Agent to handle application logs.
  - Integrated Google Pubsub to trigger Cloud functions for email verification via Mailgun upon user registration.
  - Connected Cloud SQL with Cloud function via VPC access connector for email tracking.
  - Implemented a compute instance template, health checks, managed instance group, load balancer, external IP, and Google-managed SSL certificates using Terraform.
  - Employed Customer-managed encryption keys for VMs, CloudSQL, and Cloud Storage, with a 30-day key rotation.
  - Executed rolling updates across all instances in the managed group for seamless app deployments.

This repo uses the following module for generating password hashed with salt
- maxcountryman/flask-bcrypt

## Packer runs

Install plugins
```commandline
packer init packer/gci-machine-image.pkr.hcl
```

Format the packer file
```commandline
packer fmt packer/gci-machine-image.pkr.hcl
```

Validate packer configuration
```commandline
packer validate packer/gci-machine-image.pkr.hcl
```

Build Image and upload google cloud
```commandline
packer build packer/gci-machine-image.pkr.hcl
```

More details will be added soon.
