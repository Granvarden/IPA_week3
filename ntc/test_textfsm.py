from netmiko import ConnectHandler
import pytest
from textfsmlab import oneforall

def test_r1_int():
    output = []
    for one in oneforall(1):
        print(f"{one['neighbor_name']} is connected to your {one['local_interface']}")
        output.append(f"{one['neighbor_name']} is connected to your {one['local_interface']}")
    assert "R2.ipa.com is connected to your Gig 0/2" in output
    assert "S0.ipa.com is connected to your Gig 0/0" in output
def test_r2_int():
    output = []
    for one in oneforall(2):
        print(f"{one['neighbor_name']} is connected to your {one['local_interface']}")
        output.append(f"{one['neighbor_name']} is connected to your {one['local_interface']}")
    assert "S0.ipa.com is connected to your Gig 0/0" in output
    assert "R1.ipa.com is connected to your Gig 0/1" in output
    assert "S1.ipa.com is connected to your Gig 0/2" in output


def test_s1_int():
    output = []
    for one in oneforall(3):
        print(f"{one['neighbor_name']} is connected to your {one['local_interface']}")
        output.append(f"{one['neighbor_name']} is connected to your {one['local_interface']}")
    #assert output[0] == "R2.ipa.com is connected to your Gig 0/1"
    #assert output[1] == "S0.ipa.com is connected to your Gig 0/0"
    assert "R2.ipa.com is connected to your Gig 0/1" in output
    assert "S0.ipa.com is connected to your Gig 0/0" in output


#test_r1_int()
#test_r2_int()
#test_s1_int()
