variable "region" {
  description = "Define the instance region"
  default     = "us-east-1"
}

variable "name" {
  description = "Application's name"
  default     = "Server 01"
}

variable "env" {
  description = "Application's environment"
  default     = "prod"
}

variable "ami" {
  description = "Amazon image"
  default     = "ami-0149b2da6ceec4bb0"
}

variable "instance_type" {
  description = "AWS Instance type"
  default     = "t2.micro"
}

variable "repo" {
  description = "Application's repository"
  default     = "github.com/ramosgladson/terraform"

}