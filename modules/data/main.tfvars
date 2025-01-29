

vsphere_server = "flashstack-vcenter.puretec.purestorage.com"
vsphere_user = "administrator@vsphere.local"
vsphere_password = ""

#common
osguest_id = "ubuntu64Guest"
internal_domain = "puretec.purestorage.com"
vmSubnet = "VLAN-2026"
dns_servers = ["10.21.210.98"]
vm_cluster = "Metro-Cluster-2"
dc = "Solutions-Lab"

vm_gateway = "10.21.26.1"


#vm 
vm_count = "1"
vm_name = "data-infra"
network = "10.21.26.0"
netmask = "23"
vm_ip = ["10.21.26.8"]
vmware_os_template = "linux-ubuntu-22.04lts-v25.01"
vm_cpus = 16
vm_memory = 16384
os_disk_size = "100"
data_disk_size = "1500"
datastore_os = "Metrocluster-2-DS"
datastore_data = "Metrocluster-2-DS"
contentlib_name = "SolutionsLab-ContentLib"












