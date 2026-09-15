import requests
import json

response = requests.get('http://localhost:8000/api/')
print(f"NetBox Status: {responding.status_code}")
if response.status_code == 200: 
    print("NetBox is running successfully!")
else:
    print("Failed to connect to NetBox")