

vsphere_server = "flashstack-vcenter.puretec.purestorage.com"
vsphere_user = "administrator@vsphere.local"
vsphere_password = ""

#common
osguest_id = "rhel8_64Guest"
internal_domain = "puretec.purestorage.com"
vmSubnet = "VLAN-2026"
dns_servers = ["10.21.93.16"]
vm_cluster = "Metro-Cluster-2"
dc = "Solutions-Lab"

vm_gateway = "10.21.26.1"


#vm 
vm_count = "2"
vm_name = "stac-m3"
network = "10.21.26.0"
netmask = "23"
vm_ip = ["10.21.210.165"]
vmware_os_template = "linux-rhel-9-v25.01"
vm_cpus = 16
vm_memory = 16384
os_disk_size = "100"
data_disk_size = "100"
datastore_os = "Metrocluster-2-DS"
datastore_data = "Metrocluster-2-DS"
contentlib_name = "SolutionsLab-ContentLib"












