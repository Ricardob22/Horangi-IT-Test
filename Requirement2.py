import requests #import requests module 
import json #import json

apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjUzMTUzNzU4LCJ1aWQiOjE0NzA2NzY1LCJpYWQiOiIyMDIwLTA2LTIzVDEwOjAyOjUyLjAwMFoiLCJwZXIiOiJtZTp3cml0ZSJ9.cclLoe2ixeNT8oqvoAw79vcS9o0RWOVCySP91-VSpT8" #API Key from my monday.com account
apiUrl = "https://api.monday.com/v2" #monday.com API 
headers = {"Authorization" : apiKey}

#Update the status value
query3 = 'mutation { change_column_value ( board_id: 617529303, item_id: 617529304, column_id: "status", value: "{\\\"label\\\":\\\"Done\\\"}" ) { id } }'
data = {'query' : query3}

#make request
r = requests.post(url=apiUrl, json=data, headers=headers) 
