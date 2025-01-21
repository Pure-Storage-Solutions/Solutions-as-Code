vsphere_server = "flashstack-vcenter.puretec.purestorage.com"
vsphere_user = "administrator@vsphere.local"
vsphere_password = ""

#common
osguest_id = "windows9Server64Guest"
internal_domain = "puretec.purestorage.com"
vmSubnet = "VLAN-2026"
dns_servers = ["10.21.210.98"]
vm_cluster = "Metro Cluster2"
dc = "SolutionsLab"

vm_gateway = "10.21.26.1"


#vm 
vm_count = "1"
vm_name = "commcell"
network = "10.21.26.0"
netmask = "23"
vm_ip = ["10.21.210.22"]
vmware_os_template = "windows-server-2022-standard-core-v24.12"
vm_cpus = 8
vm_memory = 16384
os_disk_size = "100"
data_disk_size = "500"
datastore_os = "Metrocluster-2-DS"
datastore_data = "Metrocluster-2-DS"
winadminpass = "VMware1!"
contentlib_name = "SolutionsLab-ContentLib"
vm_folder = "Unni-VMs"








