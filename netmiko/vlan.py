from netmiko import ConnectHandler

# device_ip = [ "172.31.21.1", "172.31.21.2","172.31.21.3","172.31.21.4","172.31.21.5" ]
device_ip = "172.31.14.3"
username = "admin"
# ไม่จำเป็นต้องใช้ตัวแปร password เมื่อมีการใช้ SSH key
# password = "cisco"

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

# รวบรวมคำสั่งตั้งค่าทั้งหมดไว้ในรายการเดียว
config_commands = [
    "vlan 101",
    "name control-data",
    "exit",
    "int vlan 101",
    "no shut",
    "exit",
    "int range gi0/1, gi0/3",
    "switch mode access",
    "switch access vlan 101"
]

with ConnectHandler(**device_params) as ssh:
    print(f"Connecting to {device_ip}...")
    
    # ส่งคำสั่งทั้งหมดในรายการด้วยเมธอด send_config_set()
    output = ssh.send_config_set(config_commands)
    
    print(output)
    print("Configuration complete.")