# Aws
>[Documentation][aws-docs]


## Aws cli
>[Documentation][aws-cli-docs]
>[Download/install aws cli][aws-cli-install-docs]
>[Youtube video reference][aws-cli-yt]


### Credentials and Config file
> It's possible to have multiples configurations and credentials
> [Docummentation][credential-docs]

* ~/.aws/credentials
```
[default]
aws_access_key_id = XYZ5645613213WERWT
aws_secret_access_key = ex+2564DGSAGGDSG59fg+as

[abcd]
aws_access_key_id = XYZ5DFKGJDLS6546SAFA
aws_secret_access_key = FDKSE++gd025sfdgGSAGGDSG59fg+as
```

* ~/.aws/config
```
[default]
region = us-east-1

[profile abcd]
region = eu-west-3
output = yaml
```

> Profile flag

--profile abcd

> It's possible to user environment variables
[Documentation][aws-cli-env-docs]

```
$ export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
$ export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
$ export AWS_DEFAULT_REGION=us-west-2
```

### Aws cli commands
>[Documentation][aws-cli-comm-docs]


```
> Show s3 running on profile1


$ aws s3 ls --profile profile1
example-bucket-1
example-bucket-2

> show ubuntu 22.04 ec2 images created in november 22 by canonical
$ aws ec2 describe-images --filters "Name = name, Values = ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server* " "Name = creation-date, Values = 2022-11*" "Name = owner-id, Values = 099720109477" --query 'Images[*].ImageId'

> show most recent ubuntu 22.04 ec2 images by canonical
$ aws ec2 describe-images --filters "Name = name, Values = ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server*" "Name = owner-id, Values = 099720109477" --query 'sort_by(Images, &CreationDate)[-1].ImageId' --output text

> run one instance with the most recent ubuntu 22.04 ec2 images by canonical
$ aws ec2 run-instances --image-id $(aws ec2 describe-images --filters "Name = name, Values = ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server*" "Name = owner-id, Values = 099720109477" --query 'sort_by(Images, &CreationDate)[-1].ImageId' --output text) --count 1 --instance-type t2.micro --key-name MyKey

> create a key pair and store private key in local file
$ aws ec2 create-key-pair --key-name MyKey2 --query 'KeyMaterial' --output text > mykey

> tag a key pair
$ aws ec2 create-tags --resources key-0efa1b260972bb020 --tags Key=ambiente,Value=prod

> show key pairs
$ aws ec2 describe-key-pairs --filters "Name = tag-key, Values = ambiente"
$ aws ec2 describe-key-pairs --filters "Name = tag-value, Values = prod"
$ aws ec2 describe-key-pairs --filters "Name = key-name, Values = MyKey"

> deleting key pairs
$ aws ec2 delete-key-pair --key-name MyKey


> show runing instances id
$ aws ec2 describe-instances --query 'Reservations[0].Instances[*].InstanceId' --output text

> tag a image
$ aws ec2 create-tags --resources $(aws ec2 describe-instances --query 'Reservations[0].Instances[*].InstanceId' --output text) --tags 'Key=ambiente, Value=prod'

> terminate instances
$ aws ec2 terminate-instances --instance-ids $(aws ec2 describe-instances --query 'Reservations[0].Instances[*].InstanceId' --output text)

> make a bucket
$ aws s3 mb s3://outlawcowboy

> remove a bucket
aws s3 rb s3://outlawcowboy

> copy from a folder to s3
$ aws s3 cp Readme.md s3://outlawcowboy

> list s3 content
$ aws s3 ls s3://outlawcowboy

> sync local folder to s3
$ aws s3 sync ~/new s3://outlawcowboy
$ aws s3 sync /home/ramos/new s3://outlawcowboy --delete

> sinc way back
$ aws s3 sync s3://outlawcowboy ~/myfolder

> delete files on s3
$ aws s3 rm s3://outlawcowboy/file.txt

> move files
$ aws s3 mv ~/myfile s3://outlawcowboy

> remove a bucket
aws s3 rb s3://outlawcowboy
$ aws s3 rb s3://outlawcowboy --force    //force flag for non empty s3


```

###












<!-- Markdown Links -->

[cedential-docs]: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html
[aws-docs]: https://docs.aws.amazon.com/index.html
[aws-cli-docs]: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html
[aws-cli-install-docs]: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
[aws-cli-env-docs]: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html
[aws-cli-yt]: https://www.youtube.com/watch?v=PWAnY-w1SGQ


