import time
import paramiko
import os

username = 'admin'
key_path = os.path.expanduser("~/.ssh/id_rsa.pub")
devices_ip = ["172.31.14.1", "172.31.14.2", "172.31.14.3", "172.31.14.4", "172.31.14.5"]

for ip in devices_ip:
    print(" Connecting to {} ...".format(ip))
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ip, username=username, key_filename=key_path)

    with client.invoke_shell() as ssh:
        print(" Connected to {} ...".format(ip))

        ssh.send("terminal length 0\n")
        time.sleep(1)
        output = ssh.recv(1000).decode('ascii')
        print(output)

        ssh.send("show ip int brief\n")
        time.sleep(1)
        output = ssh.recv(2000).decode('ascii')
        print(output)

    client.close()
