provider "aws" {
    region     = "ap-south-1"
    access_key = "12133131gfgfhggg"
    secret_key = "dgfdhffyjgjgjg323232jjhjhjkjkjkjk"
}

resource "aws_instance" "firstserver" {
    ami           = "ami-07eaf27c7c4a884cf"
    instance_type = "t2.micro"

    tags = {
      Name = "firstserver-instance"
  }
}