Vagrant.configure("2") do |config|
  config.vm.provision :shell, inline: "sudo -i"
  config.vm.provision :shell, inline: "echo -e 'deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main\ndeb http://deb.debian.org/debian buster main' >> /etc/apt/sources.list"
  config.vm.provision :shell, inline: "apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367 && apt-get update -y && apt-get install ansible -y"
  config.vm.network "private_network", virtualbox__intnet: "intnet-1", auto_config: false
  config.vm.network "private_network", virtualbox__intnet: "intnet-2", auto_config: false
end