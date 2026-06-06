#!/usr/bin/env python3

# Mock list of server hostnames in the infrastructure
server_list = ['vgh-prod-web01', 'vgh-test-db01', 'tor-prod-app01', 'vgh-prod-db02', 'vgh-dev-web02']

def get_prod_servers(servers):
    # This function should loop through the servers list and return a NEW list 
    # containing ONLY servers that have '-prod-' in their hostname.
    # code here

def count_vgh_servers(servers):
    # This function should loop through the servers list and COUNT how many 
    # hostnames start with 'vgh-'.
    # Returns: An integer representing the count.
    # code here

if __name__ == '__main__':
    print('Production Servers:', get_prod_servers(server_list))
    print('VGH Server Count:  ', count_vgh_servers(server_list))