terraform {
  required_providers {
    archive = {
      source = "hashicorp/archive"
    }
    random = {
      source = "hashicorp/random"
    }
  }
}

resource "random_string" "mystring" {
  length   = 5
  special = false
}


data "archive_file" "arquivozip" {
  type        = "zip"
  source_dir  = "data/"
  output_path = "${random_string.mystring.result}.zip"
}

output "arquivozip" {
  value = data.archive_file.arquivozip.output_size
}

output "mystring" {
  value = random_string.mystring.result
}
