from netmiko import ConnectHandler

device_ip = "172.31.14.4"
username = "admin"

device_params = {
    'device_type': 'cisco_ios',
    'ip': device_ip,
    'username': username,
    'key_file' : "/home/devasc/.ssh/id_rsa",
    'use_keys': True,
    'conn_timeout': 30,
    'global_delay_factor': 2,
    'disabled_algorithms': {
        'pubkeys': ['rsa-sha2-256', 'rsa-sha2-512']
    }
}


config_commands = [
    "router ospf 1 vrf control-data",
    "network 172.31.14.0 0.0.0.255 area 0",
    "exit",
    "int gi0/2",
    "vrf forwarding control-data",
    "ip add 172.31.14.7 255.255.255.240",
    "ip ospf 1 area 0",
    "no shut",
    "exit",
    "int loopback0",
    "ip add 1.1.1.1 255.255.255.0",
    "no shut",
    "vrf forwarding control-data",
    "ip ospf 1 area 0"
]

with ConnectHandler(**device_params) as ssh:
    print(f"Connecting to {device_ip}...")

    output = ssh.send_config_set(config_commands)
    print(output)
    
    print("Configuration complete.")