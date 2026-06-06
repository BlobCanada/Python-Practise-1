#!/usr/bin/env python3

# Inventory of network switches: { 'Device_Hostname': 'IP_Address' }
network_inventory = {
    'tor-sw-01': '10.10.1.5',
    'VGH-SW-02': '10.10.1.12',
    'tor-router-01': '192.168.1.1',
    'vgh-sw-01': '10.20.1.5',
    'vgh-sw-03': '10.10.1.25',
    'NY-SW-01': '172.16.1.4'
}

def clean_inventory(inventory):
    # This function should take the inventory dictionary, look at all the keys (hostnames),
    # and return a NEW dictionary where all hostnames are strictly lowercase.
    # The values (IPs) should stay exactly the same.
    # code here

def audit_subnet(inventory, subnet_prefix):
    # This function filters the inventory based on an IP prefix.
    # Arguments: The inventory dictionary and a string prefix (e.g., '10.10.')
    # Behavior: Loop through the dictionary. If the IP address value STARTS with the subnet_prefix,
    # add its hostname to a set.
    # Returns: A set of hostnames that match the subnet.
    # code here

def find_malformed_switches(inventory):
    # This function finds hostnames that don't match our standards.
    # Standard: A valid switch hostname must be completely lowercase AND must contain the substring '-sw-'.
    # Behavior: Compare the keys of the original raw inventory against a filtered list.
    # Returns: A list of hostnames from the original inventory keys that are either uppercase OR do not contain '-sw-'.
    # code here

if __name__ == '__main__':
    # 1. Clean the inventory tags
    cleaned_data = clean_inventory(network_inventory)
    print('Cleaned Inventory:     ', cleaned_data)
    
    # 2. Audit specific subnet
    vaughan_subnet = audit_subnet(cleaned_data, '10.10.')
    print('Devices in 10.10. Subnet:', vaughan_subnet)
    
    # 3. Find violations in the original network_inventory
    bad_devices = find_malformed_switches(network_inventory)
    print('Malformed Hostnames:    ', bad_devices)