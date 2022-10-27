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

variable "instance_type" {
  description = "AWS Instance type"
  default     = "t2.micro"
}

variable "repo" {
  description = "Application's repository"
  default     = "github.com/ramosgladson/terraform"

}

variable "security" {
  description = "Application's security group"
  default     = "sg-072c0d2e61febb98d"
}

variable "key_name" {
  description = "Application's key pair"
  default     = "Sema"
}
