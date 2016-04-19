# openstack-ansible
OpenStack Installation with Ansible

Prerequisites:-

1. One node with Ansible installed. (You can use ansible in any one of openstack nodes or in separate node)
2. 3 nodes with below configurations.

       i. VM1(Controller) - Hard disk 50GB, RAM 1 GB, 1 CPU, Interfaces 2 ( 1 NAT, 1 Host only adapter vboxnet0 )
       
       ii. VM2(Compute) - Hard disk 50GB, RAM 2 GB, 2 CPU, Interfaces 3 (1 NAT, 2 Host only adapter vboxnet0 )
       
       iii. VM3(Network) - Hard disk 50GB, RAM 2 GB, 1 CPU, Interfaces 4 (1 NAT, 3 Host only adapter vboxnet0 )

3. All 3 VMs should communicate with each other and with ansible node.

How to use :-

1. Copy the attached to your ansible node and untar the same.
2. Here you have to edit the 2 basic files.
    i. inventory/hosts :- Host file to ansible
    ii. group_vars/all:- Var file to define IPs, user names and passwords.
3. And you can simple install the OpenStack with single command from openstack_main.yml file location.

    command:
    
    ansible-playbook -i inventory/ openstack_main.yml
