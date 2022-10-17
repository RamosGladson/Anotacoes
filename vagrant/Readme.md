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
