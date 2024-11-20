import json
import subprocess
import sys
import os
import yaml

print(os.getcwd())
sol = sys.argv[1]
process = subprocess.Popen(["terraform", "output", "-json"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out, err = process.communicate()
ouput = out.decode('utf-8')

data = json.loads(ouput)
ips = data['vm_ip']['value']
names = data['vm_name']['value']
print(f"The ips are {ips} and the vms domain names are  {names} \n\n\n")
#filename = 'modules/' + sol +  '/hosts.ini'
var_filename = 'hosts.yml'
filename = 'hosts.ini'
print(filename)
print(sol)
# check if  the solution is windows
# prepare the hosts.ini with more details to login 
if sol == 'MSSQL': #or 'MSSQLDC':
    print(sol)
    with open(filename,'w') as fh:
        fh.write("[win]\n")
        for name in names:
            fh.write(name.rstrip().split('.')[0]+ '.fslab.local' + '\n')
        fh.write("[win:vars]\n")
        # fh.write("ansible_user=administrator\n")
        # fh.write("ansible_password=VMware1!\n")
        fh.write("ansible_user=vidm@FSLAB.LOCAL\n")
        fh.write("ansible_password=Osmium76$\n")
        fh.write("ansible_connection=winrm\n")
        fh.write("ansible_winrm_server_cert_validation=ignore\n")
        fh.write("ansible_port=5985\n")
        fh.write("ansible_winrm_scheme=http\n")
        fh.write("ansible_winrm_kerberos_delegation=true\n")
        fh.write("ansible_winrm_transport=kerberos\n")
        
else:
    with open(filename,'w') as fh:
        for ip in ips:
            fh.write(ip.rstrip() + '\n')

    with open(var_filename,'w') as fh:
        fh.write('hg:' + '\n')
        for ip in ips:
            fh.write(' - ' + ip.rstrip() + '\n')


#os.chdir(os.path.join(os.getcwd(), '..', '..', 'ansible')) 
# These files needs to be checked in so that the hardcoded lines can be removed in future.

direct_asm_path = '/root/Oracle-build/ansible'
os.chdir(direct_asm_path)
print(os.getcwd())

def append_ip_to_hosts(ip_addresses, hosts_file= os.getcwd() + '/inventory-asm-demo/hosts.yml'):
    '''
    This method will remove the old hosts.yml file (if it exists) and create a new one with the provided IP addresses.
    '''
    if os.path.exists(hosts_file):
        os.remove(hosts_file)  # Remove the old file
        print(f"Old file {hosts_file} removed.")

   
    hosts_data = {
        'all': {
            'children': {
                'dbfs': {
                    'hosts': {}
                }
            }
        }
    }

    # Append new IP addresses to the hosts section
    for ip_address in ip_addresses:
        hosts_data['all']['children']['dbfs']['hosts'][ip_address] = {'ansible_ssh_user': 'ansible'}
        print(f"IP address {ip_address} added successfully to {hosts_file}")

    # Write the new data to the hosts file
    with open(hosts_file, 'w') as file:
        file.write('---\n')  # Add the YAML document start marker
        yaml.dump(hosts_data, file, default_flow_style=False)

def create_and_update_host_vars(ip_addresses, domain_names):
    '''
    Will create a new host_vars template with new IP address and domain names
    '''
    base_dir =  os.getcwd() +  '/inventory-asm-demo/host_vars'
    for ip_address, domain_name in zip(ip_addresses, domain_names):
        ip_dir = os.path.join(base_dir, ip_address)
        databases_file_path = os.path.join(ip_dir, 'databases.yml')       
        tnsnames_file_path = os.path.join(ip_dir, 'tnsnames.yml')
        os.makedirs(ip_dir, exist_ok=True)

        # Define databases_content with proper structure and indentation
        databases_content = {
            'rman_retention_policy': "RECOVERY WINDOW OF 14 DAYS",
            'rman_channel_disk': "format '/u01/rmanbackup/%d/%d_%T_%U'",
            'rman_controlfile_autobackup_disk': "'/u01/rmanbackup/%d/%d_%F'",
            'rman_device_type_disk': 'PARALLELISM 1 BACKUP TYPE TO COMPRESSED BACKUPSET',
            'oracle_databases': [
                '- "{{ oracle_database_db1 }}"'
            ],
            'oracle_pdbs': [
                '- "{{ oracle_pdb_db1_orclpdb }}"'
            ],
            'oracle_listeners_config': {
                'LISTENER': {
                    'home': 'db21-gi-ee',
                    'address': [
                        {'- host': domain_name, 'port': 1521, 'protocol': 'TCP'}
                    ]
                }
            },
            'oracle_tnsnames_config': {
                'ORCLPDB': {
                    'connect_timeout': 5,
                    'retry_count': 3,
                    'address': [
                        {'- host': domain_name, 'port': 1521, 'protocol': 'TCP'}
                    ]
                }
            },
            'tnsnames_installed': [
                {'- home': 'db2103-gi-ee', 'state': 'present', 'tnsname': 'ORCLPDB'}
            ]
        }

        with open(databases_file_path, 'w') as db_file:
            db_file.write('---\n')  # Add the YAML document start marker
            yaml.dump(databases_content, db_file, default_flow_style=False)

        print(f"Created {databases_file_path} with initial content.")

        # Define tnsnames_content with correct structure
        tnsnames_content = {
            'oracle_tnsnames_config': {
                'ORCLPDB': {
                    'failover': 'yes',
                    'connect_timeout': 5,
                    'retry_count': 3,
                    'address': [
                        {'- host': domain_name, 'port': 1521, 'protocol': 'TCP'}
                    ]
                }
            },
            'tnsnames_installed': [
                {'- home': 'db2103-gi-ee', 'state': 'present', 'tnsname': 'ORCLPDB'}
            ]
        }

        with open(tnsnames_file_path, 'w') as tns_file:
            tns_file.write('---\n')  # Add the YAML document start marker
            yaml.dump(tnsnames_content, tns_file, default_flow_style=False)

        print(f"Created {tnsnames_file_path} with initial content.")

append_ip_to_hosts(ip_addresses=ips)
create_and_update_host_vars(ip_addresses=ips, domain_names=names)




