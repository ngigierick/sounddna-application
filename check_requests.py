import requests

res = requests.get("https://httpbin.org/get")
print("Status code:", res.status_code)
