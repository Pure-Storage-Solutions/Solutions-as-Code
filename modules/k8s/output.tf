output "vm_ip" {
  value = "${module.vm.vm_ip}"
}
output "vm_name" {
  value = "${module.vm.vm_name}"
}

output "new_ip_address" {
  value = "${module.vm.*.clone.0.customize.0.network_interface.0.ipv4_address}"
}