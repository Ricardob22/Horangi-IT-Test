import requests #import requests module 
import json #import json

apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjUzMTUzNzU4LCJ1aWQiOjE0NzA2NzY1LCJpYWQiOiIyMDIwLTA2LTIzVDEwOjAyOjUyLjAwMFoiLCJwZXIiOiJtZTp3cml0ZSJ9.cclLoe2ixeNT8oqvoAw79vcS9o0RWOVCySP91-VSpT8" #API Key from my monday.com account
apiUrl = "https://api.monday.com/v2" #monday.com API 
headers = {"Authorization" : apiKey}

#Writing the query to list the items
query2 = '{boards(limit:1) { name id description items { name  } } }'
data = {'query' : query2}

#posting the requests and output it
r = requests.post(url=apiUrl, json=data, headers=headers) 
#print the items
print(r.json())
