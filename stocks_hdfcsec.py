### This is hdfc securities open api which is still not fully live ###
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
# "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

# sending post request and generating otp on mobile/email
print(login_url)
r = requests.post(url=login_url, json=data, headers=headers)
print(r.status_code)
print(r.text)

#input otp
two_fa_otp = input("Enter otp received on mobile: ")

#validate otp

data = {"answer": two_fa_otp, "api_key": api_key}

validate_url = f"https://developer.hdfcsec.com/oapi/v1/login/twofa/validate?api_key={api_key}&token_id={token_id}"

print(validate_url)
r = requests.post(url=validate_url, json=data)
print(r.status_code)
print(r.text)


