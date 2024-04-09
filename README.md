# webapp_aws_cicd
Cloud native web application

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

More details will be added soon..
