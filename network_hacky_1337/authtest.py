import requests

req1 = requests.get('http://1.1.1.3/ac_portal/default/pc.html?template=default&tabs=pwd&vlanid=0&url=http://www.msftconnecttest.com%2fredirect')

print(req1.text)