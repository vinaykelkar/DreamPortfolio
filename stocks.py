import requests
import pyotp
import time

api_key = '7da70ed5709644f69514bdefe5ca491a'
generate_token = f"https://developer.hdfcsec.com/oapi/v1/login?api_key={api_key}"
response = requests.get(generate_token)

# Check if the request was successful (status code 200) and generate token id
if response.status_code == 200:
    print("GET request successful!")
    print("Response:")
    token_id = response.text
    token_data = eval(token_id)
    token_id = token_data['tokenId']
    print("======")
else:
    print(f"GET request failed with status code {response.status_code}")

# Check if token id can be used to successfully login

# data to be sent to api
login_url = f"https://developer.hdfcsec.com/oapi/v1/login/validate?api_key={api_key}&token_id={token_id}"
username = '47610437'
password = 'Vks@9028'
data = {"username" : username, "password" : password}
headers = {
    "Content-Type": "application/json"
}

# sending post request and saving response as response object
print(login_url)
r = requests.post(url=login_url, json=data, headers=headers)
print(r.status_code)
print(r.text)


