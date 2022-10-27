data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server*"]

  }

  owners = ["099720109477"]

}

data "aws_key_pair" "sema" {
  key_name           = "Sema"
  include_public_key = true

}

data "aws_security_group" "sema" {
  security_groups = ["terraform"]
}

resource "aws_instance" "server" {
  ami             = data.aws_ami.ubuntu.id
  instance_type   = var.instance_type
#  security_groups = data.aws_security_group.sema.id
  key_name        = data.aws_key_pair.sema.key_name

  network_interface {
    network



  tags = {
    Name        = var.name
    Environment = var.env
    Provisioner = "Terraform"
    Repo        = var.repo
  }
}
