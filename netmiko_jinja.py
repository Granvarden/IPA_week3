from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))

template = env.get_template('router_config.j2')

router_data = {
    "hostname": "R2",
    "vrf_name": "control-data",
    "inside_interface": "GigabitEthernet0/1",
    "inside_ip": "172.31.14.9",
    "inside_mask": "255.255.255.240",
    "outside_interface": "GigabitEthernet0/3",
    "outside_ip": "203.0.113.2",  # NAT-facing IP
    "outside_mask": "255.255.255.252",
    "subnet": "172.31.14.0",
    "wildcard": "0.0.0.15"
}


config = template.render(router_data)
config_lines = config.splitlines()


device = {
    'device_type': 'cisco_ios',
    'ip': '172.31.14.2',  
    'username': 'admin',
    'use_keys': True,
    'key_file': '/home/devasc/.ssh/id_rsa',
}

with ConnectHandler(**device) as conn:
    print(f"Connecting to {device['ip']}...")
    output = conn.send_config_set(config_lines)
    print(output)
