import requests


url = 'http://127.0.0.1:8000/add_person'  # localhost and the defined port + endpoint
# url = 'https://pottsen-atrium-hw2.azurewebsites.net/helloname'
body = {
    'first': 'Peter',
    'last': 'Ottsen',
    'age': 30
}
response = requests.post(url, json=body)
print(response.text)