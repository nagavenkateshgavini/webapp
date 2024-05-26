# 12 factor Cloud native web application
The 12-factor app is a methodology for building software-as-a-service (SaaS) applications that are cloud-native and distributed. The 12 factors are a set of best practices that are independent of programming languages and software stacks, and can be applied to a variety of apps. The goal of the 12-factor app is to make applications more portable, resilient, scalable, and robust when deployed to the web. Used google cloud platform to develop this. Made with Love and Fun.

## Architecture Diagram:
![csye6225](https://github.com/nagavenkateshgavini/webapp/assets/20241067/e04fb7e5-3b10-4112-b42e-f175db47cb4c)



## This repository can act as tutorial or example project for following concepts
Employed 12-factor methodology to create user auth CI/CD project with cloud and devops best practices.

Implementation details:
- Developed a robust RESTful API using Python Flask, Postgresql and Pytest
- Utilized REST Assured for comprehensive integration testing, ensuring reliability and performance
- Crafted custom compute engine images using HashiCorp Packer
- Implemented systemd service files for smooth application startup
- Established secure VPCs, subnets, and CloudSQL instances
- Enabled VPC peering and private service access for enhanced security
- Leveraged Cloud DNS for seamless domain resolution
- Configured Ops Agent for streamlined application logging, ensuring observability and troubleshooting ease
- Orchestrated message publication to Google Pub/Sub topics
- Triggered Cloud Functions for automated email verification using Sinch Mailgun
- Engineered compute instance templates, and managed instance groups, and load balancers for autoscaling based on the CPU utilization metrics.
- Implemented SSL certificates managed by GCP
- Enabled automated rolling updates on merge to ensure seamless deployment

**Other repositories in this project.**
- [Terraform code to build Infrastructure on GCP platform](https://github.com/nagavenkateshgavini/tf-gcp-infra)
- [Cloud Function Repo or Serverless code](https://github.com/nagavenkateshgavini/serverless)


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

Note: In an ideal situation when a developer raises a PR, GitHub actions automatically trigger the integration tests, build GCI image, and deploy in the GCP cloud automatically. Please check out the GitHub actions for more details.
