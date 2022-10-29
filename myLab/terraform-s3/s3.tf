resource "aws_s3_bucket" "meudrive221028" {
  bucket = "meudrive221028"

  tags = {
    Name = "Meu_drive"
  }
}

resource "aws_s3_bucket_acl" "meudrive221028_acl" {
  bucket = aws_s3_bucket.meudrive221028.id
  acl    = "private"

}
