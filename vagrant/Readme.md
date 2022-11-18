# Vagrant
> Comandos vagrant

```
sudo apt install vagrant                 | Install vagrant
vagrant box list                         | list of images
vagrant box add debian/jessie64          | add debian jessie 64 image from Vagrant repository
vagrant box update                       | updates the bos for the current vagrant environment
vagrant box outdated                     | show outdated current vagrant environment box
vagrant box outdated --global            | show outdated every instaled box
vagrant box prune                        | uninstall old box versions
vagrant box remove debian/jessie64       | uninstall especific box "debian/jessie64"
vagrant plugin install vagrant-disksize  | install vagrant-disksize plugin
vagrant plugin list                      | show plugins list
vagrant up                               | start vm
vagrant halt                             | shutdown vm
vagrant reload                           | reboot the vm (vagrant halt && vagrant up)
vagrant suspend                          | suspends vm (save)
vagrant resume                           | return from saved mode (return from suspended)
vagrant destroy                          | delete vm
vagrant destroy -f                       | force delete (no propmt)
vagrant upload /source/file /dest/file   | copy from source (vagrant machine) to vm
vagrant status                           | show vm status



```

## Vagrantfile
> Vagrant configuration file


* [configure][configure-docs]
> makes an object with configuration "1" or "2"

```
Vagrant.configure("2") do |config|                                       
  # ...
end
```

* [config][config-docs]

```
$script = <<-SCRIPT
echo I am provisioning...
date > /etc/vagrant_provisioned_at
SCRIPT


Vagrant.configure("2") do |config|
  config.disksize.size = "50GB"                                                     | one way to resize disk (this way, all config objects)
  config.vm.provision "shell", path: "https://example.com/provisioner.sh"
  config.vm.provision "shell", inline: $script
  config.vm.provision "shell", path: "./script"
  config.vm.provision "shell", inline: "echo hello world"
  config.vm.define "xyz" do |abcd|                                                  | object object abcd inherited config configuration
    abcd.vm.box = "ubuntu/trusty64"                                                 | "xyz" used for ssh, abcd only in this scope
    abcd.vm.hostname = "asdfg"                                                      | set "asdfg" at /ect/hostname and 127.0.0.1  asdfg   at /etc/hosts
    abcd.vm.network "public_network", brigde: "ens01", ip: "10.10.30.3"             | set bridge at ens01
    abcd.vm.network "public_network", brigde: "ens01", type: "dhcp"                 | set bridge with dhcp
    abcd.vm.disk :disk, size: "100GB", primary: true                                | another way to resize disk
    abcd.vm.disk :disk, size: "10GB", name "extra_disk"                             | attaching new disk
    (0..3).each do |i|
      abc.vm.disk :disk, size: "10GB", name: "disk-#{i}"                            | attaching extra disks with ruby
    end
    abcd.vm.disk :dvd, name: "xyziso", file: "./xyziso.iso"                         | attaching an iso as an optical driver 
  end

end

```




<!--  Links  -->


[configure-docs]: https://developer.hashicorp.com/vagrant/docs/vagrantfile/version
[config-docs]: https://developer.hashicorp.com/vagrant/docs/vagrantfile/machine_settings
