import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Location_code':2, 'DateOfMonth':9, 'Weekday':6, 'Hour':22})

print(r.json())