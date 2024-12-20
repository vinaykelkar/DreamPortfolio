# package import statement
from SmartApi import SmartConnect  # or from SmartApi.smartConnect import SmartConnect
import pyotp
from logzero import logger
import http.client
import mimetypes
import pandas as pd
import requests
from datetime import datetime

# get current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
# convert datetime obj to string
str_current_datetime = str(current_datetime)

#angel one credentials required to login
api_key = 'xor6EnU0'
username = 'S63128103'
pwd = '0639'

#calling smarapi to generate token to login instead of otp
smartApi = SmartConnect(api_key)
try:
    token = "QOQPSUPN5S5BWNKRECXFXMBD7A"
    totp = pyotp.TOTP(token).now()
except Exception as e:
    logger.error("Invalid Token: The provided token is not valid.")
    raise e

#login api call and generating session to trade
data = smartApi.generateSession(username, pwd, totp)
refreshToken= data['data']['refreshToken']
#fetch the feedtoken
feedToken=smartApi.getfeedToken()
#fetch User Profile
userProfile= smartApi.getProfile(refreshToken)


# Get whole list of stock symbols and data from angel one
url = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'
master_list = requests.get(url).json()
master_df = pd.DataFrame.from_dict(master_list)
master_df['expiry'] = pd.to_datetime(master_df['expiry'], format='mixed').apply(lambda x:x.date())
master_df = master_df.astype({'strike':float})
master_df.to_csv(r'C:\\Users\\vinay\\Documents\\VinayFirstAlgo\\DreamPortfolio\\DreamPortfolio\\instruments_csv\\' + f'angel_one_{str_current_datetime}.csv', header=True, index=False)
print("File created ")


#get last traded price of SBI equity stock

print(smartApi.ltpData('NSE','SBIN-EQ',3045))

#get top nifty gainers and nifty losers
# logout
try:
    logout = smartApi.terminateSession('S63128103')
    logger.info("Logout Successfull")
except Exception as e:
    logger.exception(f"Logout failed: {e}")


