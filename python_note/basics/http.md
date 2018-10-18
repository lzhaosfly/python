# HTTP

## 0. install

`conda install requests`

## 1. requests

[requests library](http://docs.python-requests.org/en/master/)

```python
import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass')) # also working for download a file
r.status_code # 200
r.headers['content-type'] # 'application/json; charset=utf8'
r.encoding # 'utf-8'
r.text # u'{"type":"User"...'
r.json() # {u'private_gists': 419, u'total_private_repos': 77, ...}

url = "https://icanhazdadjoke.com/"

response = requests.get(url, headers={"Accept": "application/json"})

data = response.json()

print(data["joke"])
print(f"status: {data['status']}")
```
