import requests
r = requests.get('https://iamawesome.com')
print(r.text)
# r.headers['content-type']
# 'application/json; charset=utf8'
# r.encoding
# 'utf-8'
# r.text
# '{"authenticated": true, ...'
# r.json()
# {'authenticated': True, ...}