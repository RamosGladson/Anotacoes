resource "aws_s3_bucket" "samba_mylab" {
  bucket = "samba-mylab-teste"

  tags = {
    Name        = "samba bucket"
    Environment = "dev"
  }
}

resource "aws_s3_bucket_acl" "samba_mylab_acl" {
  bucket = aws_s3_bucket.samba_mylab.id
  acl    = "private"
}