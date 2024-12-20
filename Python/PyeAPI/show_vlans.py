import pyeapi
import json

pyeapi.load_config('eapi.conf')

connect = pyeapi.connect_to('leaf1')
cmd_result = connect.enable('show vlan')

# print(json.dumps(cmd_result[0]['result']['vlans'], indent=2))

for vlan, vlan_values in cmd_result[0]['result']['vlans'].items():
    print(f"id: {vlan} | name: {vlan_values['name']}")