from netmiko import ConnectHandler

device_ip = "172.31.14.5"
username = "admin"

device_params = {
    'device_type': 'cisco_ios',
    'ip': device_ip,
    'username': username,
    'key_file': "/home/devasc/.ssh/id_rsa",
    'use_keys': True,
    'conn_timeout': 30,
    'global_delay_factor': 2,
    'disabled_algorithms': {
        'pubkeys': ['rsa-sha2-256', 'rsa-sha2-512']
    }
}

config_commands = [
    "conf t",
    "router ospf 1 vrf control-data",
    "network 172.31.14.0 0.0.0.255 area 0",
    "network 192.168.122.0 0.0.0.255 area 0",
    "default-information originate always",
    "exit",

    "interface GigabitEthernet0/2",
    "shutdown",  # ปิดก่อนเปลี่ยน VRF
    "vrf forwarding control-data",
    "ip address 172.31.14.8 255.255.255.240",
    "no shutdown",
    "ip ospf 1 area 0",
    "exit",

    "interface Loopback0",
    "ip address 1.1.1.2 255.255.255.0",
    "no shutdown",
    "ip ospf 1 area 0",

    # PAT configuration
    "ip access-list standard NAT_ACL",
    "permit 172.31.14.0 0.0.0.15",  # Allow subnet 172.31.14.0/28
    "exit",

    "interface GigabitEthernet0/3",  # Assuming this is the outside NAT interface
    "ip nat outside",
    "exit",

    "interface GigabitEthernet0/2",  # Assuming this is the inside NAT interface
    "ip nat inside",
    "exit",

    "ip nat inside source list NAT_ACL interface GigabitEthernet0/1 overload",

    # SSH/Telnet restrictions
    "ip access-list standard MGMT_ACCESS",
    "permit 192.168.1.0 0.0.0.255",  # Lab306
    "permit 172.31.14.0 0.0.0.15",   # Management plane subnet
    "exit"
]

with ConnectHandler(**device_params) as ssh:
    print(f"Connecting to {device_ip}...")

    output = ssh.send_config_set(config_commands)
    print(output)
