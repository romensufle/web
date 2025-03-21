import requests

print(requests.delete('http://127.0.0.1:8080/api/v2/users/5').json())  # all ok