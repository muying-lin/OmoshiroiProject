import urllib.request

response = urllib.request.urlopen('')
html = response.read().decode()

print(html)

req = urllib,request.Request('')
response = urllib.request.urlopen(req)


