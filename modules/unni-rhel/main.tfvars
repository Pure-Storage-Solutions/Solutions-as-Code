

vsphere_server = "vcenter-shared.puretec.purestorage.com"
vsphere_user = "administrator@vsphere.local"
vsphere_password = ""

#common
osguest_id = "rhel9_64Guest"
internal_domain = "puretec.purestorage.com"
vmSubnet = "VLAN-2026"
dns_servers = ["10.21.93.16"]
vm_cluster = "vCenter-Shared-Cluster"
dc = "SuperMicro"


vm_gateway = "10.21.210.1"


#vm 
vm_count = "1"
vm_name = "unni-rhel"
network = "10.21.26.0"
netmask = "23"
vm_ip = ["10.21.210.22"]
#vmware_os_template = "linux-rocky-8-v24.09"
#vmware_os_template = "linux-ubuntu-22.04-lts-v23.01"
vmware_os_template = "linux-rhel-9-v25.03"
#vm_cpus = 32
vm_cpus = 4
vm_memory = 65536
os_disk_size = "250"
data_disk_size = "150"
datastore_os = "Datastore"
datastore_data = "Datastore"
contentlib_name = "Shared-vCenter-ContentLib"












