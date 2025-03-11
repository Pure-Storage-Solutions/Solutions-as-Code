

vsphere_server = "vcenter-shared.puretec.purestorage.com"
vsphere_user = "administrator@vsphere.local"
vsphere_password = ""

#common
osguest_id = "ubuntu64Guest"
internal_domain = "puretec.purestorage.com"
vmSubnet = "VLAN-2026"
dns_servers = ["10.21.93.16"]
vm_cluster = "vCenter-Shared-Cluster"
dc = "SuperMicro"

vm_gateway = "10.21.26.1"


#vm 
vm_count = "1"
vm_name = "kube"
network = "10.21.26.0"
netmask = "23"
vmware_os_template = "linux-ubuntu-22.04lts-v25.01"
vm_cpus = 8
vm_memory = 32000
os_disk_size = "250"
data_disk_size = "150"
datastore_os = "Datastore"
datastore_data = "Datastore"
contentlib_name = "Shared-vCenter-ContentLib"












