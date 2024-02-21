packer {
  required_plugins {
    googlecompute = {
      source  = "github.com/hashicorp/googlecompute"
      version = "~> 1"
    }
  }
}

variable mysql_host {
  type    = string
  default = env("MYSQL_HOST")
}

variable mysql_user {
  type    = string
  default = env("MYSQL_USER")
}

variable mysql_password {
  type    = string
  default = env("MYSQL_PASSWORD")
}

variable mysql_db {
  type    = string
  default = env("MYSQL_DB")
}

variable flask_app {
  type    = string
  default = env("FLASK_APP")
}

variable log_file {
  type    = string
  default = env("LOG_FILE")
}

variable gcp_sa_key {
  type    = string
  default = env("GCP_SA_KEY")
}

source "googlecompute" "centos-stream-8" {
  project_id   = "csye-project-413917"
  source_image = "centos-stream-8-v20240110"
  ssh_username = "packer"
  zone         = "us-east1-b"
  account_file = "${var.gcp_sa_key}"
  network      = "default"
}

build {
  name = "csye-gce-image"
  sources = [
    "sources.googlecompute.centos-stream-8"
  ]

  provisioner "file" {
    source      = "webapp.zip"
    destination = "webapp.zip"
  }

  provisioner "shell" {
    script = "packer/install_python.sh"
    environment_vars = [
      "MYSQL_HOST=${var.mysql_host}",
      "MYSQL_USER=${var.mysql_user}",
      "MYSQL_PASSWORD=${var.mysql_password}",
      "MYSQL_DB=${var.mysql_db}",
      "FLASK_APP=${var.flask_app}",
      "LOG_FILE=${var.log_file}"
    ]
  }

  provisioner "shell" {
    script = "packer/install_mysql.sh"
    environment_vars = [
      "MYSQL_HOST=${var.mysql_host}",
      "MYSQL_USER=${var.mysql_user}",
      "MYSQL_PASSWORD=${var.mysql_password}",
      "MYSQL_DB=${var.mysql_db}",
      "FLASK_APP=${var.flask_app}",
      "LOG_FILE=${var.log_file}"
    ]
  }

  provisioner "shell" {
    script = "packer/create_user.sh"
  }

  provisioner "shell" {
    script = "packer/run_service.sh"
    environment_vars = [
      "MYSQL_HOST=${var.mysql_host}",
      "MYSQL_USER=${var.mysql_user}",
      "MYSQL_PASSWORD=${var.mysql_password}",
      "MYSQL_DB=${var.mysql_db}",
      "FLASK_APP=${var.flask_app}",
      "LOG_FILE=${var.log_file}"
    ]
  }
}
