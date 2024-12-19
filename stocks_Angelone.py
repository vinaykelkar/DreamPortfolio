# package import statement
from SmartApi import SmartConnect  # or from SmartApi.smartConnect import SmartConnect
import pyotp
from logzero import logger
import http.client
import mimetypes
import pandas as pd
import requests

api_key = 'xor6EnU0'
username = 'S63128103'
pwd = '0639'
smartApi = SmartConnect(api_key)
try:
    token = "QOQPSUPN5S5BWNKRECXFXMBD7A"
    totp = pyotp.TOTP(token).now()
except Exception as e:
    logger.error("Invalid Token: The provided token is not valid.")
    raise e

#login api call
data = smartApi.generateSession(username, pwd, totp)
refreshToken= data['data']['refreshToken']
#fetch the feedtoken
feedToken=smartApi.getfeedToken()
#fetch User Profile
userProfile= smartApi.getProfile(refreshToken)


# Get whole list of stock symbols and data from angel one
url = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'
master_list = requests.get(url).json()
df = pd.DataFrame.from_dict(master_list)
df['expiry'] = pd.to_datetime(df['expiry'], format='mixed').apply(lambda x:x.date())
df = df.astype({'strike':float})
df1 = df[(df['name']=="SBIN" & df['instrumenttype']=="")]
#unique_values = df['instrumenttype'].unique()
print(df1)
#get LTP of SBIN

# logout
try:
    logout = smartApi.terminateSession('S63128103')
    logger.info("Logout Successfull")
except Exception as e:
    logger.exception(f"Logout failed: {e}")


