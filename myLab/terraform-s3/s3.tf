terraform {
  required_version = "1.3.3"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.37.0"
    }

  }
}

resource "aws_s3_bucket" "meudrive221028" {
  bucket = "meudrive221028"

  tags = {
    Name        = "Meu_drive"
    Created     = "30/10/2022"
    Last_update = "30/10/2022"
  }
}

resource "aws_s3_bucket_acl" "meudrive221028_acl" {
  bucket = aws_s3_bucket.meudrive221028.id
  acl    = "private"

}

