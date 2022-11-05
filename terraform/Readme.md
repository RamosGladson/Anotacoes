# Terraform
> Declarative language


## O Que é terraform

- A ferramenta de infraestrutura como código mais usada no mundo DevOps
- Rápido, eficiente e replicável
- Define, provisiona, mantem e versiona infraestrutura
- Utiliza linguagem HCL (Hashicorp Configuration Language)
- Trabalha de forma declarativa
- Hashicorp disponibiliza extensa lista de prividers oficiais

## Vantagens do Terraform

- Simplicidade da linguagem HCL
- É multicloud
- Cria recursos de forma declarativa
- Documentação clara e bem estruturada
- Pode ser usado em conjunto com outras ferramentas IaC
- Idempotente (capacidade de ser aplicado várias vezes sem que o resultado se altere)
- Livre de erros humanos

## Tipos de Blocos

- Terraform
- Providers
- Resource
- Data
- Module
- Variable
- Output
- Locals

> Overview

```
terraform {

}

provider "aws" {

}

resource "aws_instance" "name" {

}

data "aws_ami" "name" {

}

module "vpc" {

}

variable "ip" {

}

output "name" {

}

locals {

}

```

> terraform {}
> [terraform block documentation][terraform-doc]

- required_version
- required_provider
- backend
- cloud
- experiments
- provider_meta


```
terraform {
    required_version  = ">= 1.0.0"

    required_provider {
        aws = {
            version = ">= 3.50.0"
            source = "hashicorp/aws"            
        }
        azure = {
            version = "2.70.0"
            source = "hashicorp/aws"
        }
    }

    backend "s3" {

    }
}

```

> Providers

- Aws
- Azure
- Kubernetes
- Etc





## Terraform cli
> [Terraform CLI documentation][terraform-cli-doc]
> Main commands

```
terraform -help                         | show help
terraform init                          | prepare working dir
terraform validate                      | check if config is valid
terraform plan                          | show changes required by the curent config
terraform apply                         | 
terraform destroy                       | Destroy previous infraestructure

terraform fmt                           | reformat config files
terraform init -help                    | get help for init command
```




<!-- Markdown Links -->

[terraform-doc]: https://developer.hashicorp.com/terraform/language/settings
[terraform-cli-doc]: https://developer.hashicorp.com/terraform/cli
