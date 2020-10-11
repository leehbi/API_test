import requests

resp = requests.get('http://localhost:5000/data')

print(resp.status_code)
print(resp.history)
