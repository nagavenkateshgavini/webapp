packer {
  required_plugins {
    googlecompute = {
      source  = "github.com/hashicorp/googlecompute"
      version = "~> 1"
    }
  }
}

variable gcp_sa_key {
  type    = string
  default = env("GCP_CREDENTIALS")
}

variable project_id {
  type    = string
  default = env("GCP_PROJECT_ID")
}

variable build_network {
  type    = string
  default = env("GCP_IMAGE_BUILD_NETWORK")
}

variable build_image_zone {
  type    = string
  default = env("BUILD_IMAGE_ZONE")
}

variable source_gci_image {
  type    = string
  default = env("SOURCE_GCI_IMAGE")
}

variable source_image_family {
  type    = string
  default = env("SOURCE_IMAGE_FAMILY")
}

variable log_file {
  type    = string
  default = env("LOG_FILE")
}


source "googlecompute" "centos-stream-8" {
  project_id          = "${var.project_id}"
  source_image        = "${var.source_gci_image}"
  source_image_family = "${var.source_image_family}"
  ssh_username        = "csye6225"
  zone                = "${var.build_image_zone}"
  account_file        = "${var.gcp_sa_key}"
  network             = "${var.build_network}"
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
  }

  provisioner "shell" {
    script = "packer/create_user.sh"
  }

  provisioner "shell" {
    script = "packer/run_service.sh"
    environment_vars = [
      "LOG_FILE=${var.log_file}"
    ]
  }
}
