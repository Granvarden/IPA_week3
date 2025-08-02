from netmiko import ConnectHandler
import re

routers = [
    {
        'device_type': 'cisco_ios',
        'ip': '172.31.14.4',
        'username': 'admin',
        'use_keys': True,
        'key_file': '/home/devasc/.ssh/id_rsa',
    },
    {
        'device_type': 'cisco_ios',
        'ip': '172.31.14.5',
        'username': 'admin',
        'use_keys': True,
        'key_file': '/home/devasc/.ssh/id_rsa',
    }
]

for router in routers:
    print(f"\nConnecting to {router['ip']}...")
    with ConnectHandler(**router) as conn:
        output = conn.send_command("show ip interface brief")
        print("\n--- ACTIVE INTERFACES ---")
        interfaces = re.findall(r"(\S+)\s+\S+\s+\S+\s+\S+\s+up\s+up", output)
        for intf in interfaces:
            print(f"Interface: {intf}")

        version_output = conn.send_command("show version")
        uptime_match = re.search(r"uptime is (.+)", version_output)
        if uptime_match:
            print(f"\n Uptime: {uptime_match.group(1)}")
        else:
            print("\n Could not find uptime information.")
