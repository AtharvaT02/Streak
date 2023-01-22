
# TESTCASES

import requests

1. Create a DNS record

endpoint = "http://localhost:8000/api/dnsrecord/"
data = {"domain_name": "example1.com", "ip_address": "11.11.11.11"}
response = requests.post(endpoint, json=data)
print(response.json())


2. Retrieve a DNS record
endpoint = "http://localhost:8000/api/dnsrecord/example1.com/"
response = requests.get(endpoint)
print(response.json())

3. Retrieve a DNS record that does not exist in the database but is a valid domain name

endpoint = "http://localhost:8000/api/dnsrecord/youtube.com/"
response = requests.get(endpoint)
print(response.json())

4. Retrieve a DNS record that does not exist in the database but is a not valid domain name

endpoint = "http://localhost:8000/api/dnsrecord/invalid.com/"
response = requests.get(endpoint)
print(response.json())
