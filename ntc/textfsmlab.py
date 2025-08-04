from netmiko import ConnectHandler
import os

def oneforall(dev):
    os.environ['NET_TEXTFSM'] = os.path.dirname(os.path.abspath(__file__))


    R1 =    {
                'device_type': 'cisco_ios',
                'ip': '172.31.14.4',
                'username': 'admin',
                'key_file': os.path.expanduser("~/.ssh/id_rsa.pub"),
                'use_keys': True,
            }
    R2 =    {
                'device_type': 'cisco_ios',
                'ip': '172.31.14.5',
                'username': 'admin',
                'key_file': os.path.expanduser("~/.ssh/id_rsa.pub"),
                'use_keys': True,
            }
    S1 =    {
                'device_type': 'cisco_ios',
                'ip': '172.31.14.3',
                'username': 'admin',
                'key_file': os.path.expanduser("~/.ssh/id_rsa.pub"),
                'use_keys': True,
            }
    def whoismyneighbors(device):
        
        with ConnectHandler(**device) as connection:
            output = connection.send_command('sh cdp neighbors', use_textfsm=True)
            connection.exit_config_mode()
            return output
    if dev == 1:
        print("This is R1")
        return whoismyneighbors(R1)
    elif dev == 2:
        print("This is R2")
        return whoismyneighbors(R2)
    elif dev == 3:
        print("This is S1")
        return whoismyneighbors(S1)