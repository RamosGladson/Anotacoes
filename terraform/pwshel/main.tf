resource "null_resource" "nulo" {

  provisioner "remote-exec" {
    inline = [ps]
  }

}





