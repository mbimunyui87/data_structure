Vagrant.configure("2") do |config|
  config.vm.box = "centos/8"  # CentOS 8 box
  config.vm.network "public_network", ip: "192.658.10.15"  # Public network with the specified IP address

  config.vm.synced_folder "/c/Users/yembu/Documents/vms/", "/vagrant"  # Synced folder configuration

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"  # Set memory size to 1024 MB
    vb.cpus = 2  # Set number of CPUs to 2
  end
end
