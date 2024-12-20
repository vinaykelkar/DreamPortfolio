from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
import simplejson

# get current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
# convert datetime obj to string
str_current_datetime = str(current_datetime)
nse_headers = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br, zstd',
'accept-language': 'en-US,en;q=0.9',
'cookie': '_ga=GA1.1.1094014996.1700135308; _ga_PJSKY6CFJH=GS1.1.1700209663.3.1.1700210336.60.0.0; _ga_QJZ4447QD3=GS1.1.1708066749.12.0.1708066749.0.0.0; defaultLang=en; AKA_A2=A; _abck=A3A2C2A2228DC9EF0229549EA08AE637~0~YAAQLwkuF+r8rayTAQAAHTOj5A30YhYfdeBf1otNAKBF11+DUY1Gi8Ef0OOfTpNTHDJZj7bbYisa9aubHeWefoYih7bqVZmaWv2xthOpX6aICDXLJwaE9SlLERG4E8BI/VMPpMlcM89LCV7VXqMGjw1n/rq3XHUo92bUi/8manyiyc+0QA8IdZ+w9tJm5iHvK1cNsLxQCaTrktlC2U913nthHpwPqOvYPAk+FjccPoCwLp432IMkPRPG4O0LhJaDnFeEEGhBmu3d6oRJmJsyAMXpy6E2qXiwEpp13e2EVql2jsvShUDOALT0azbu8F/LOIZuDh55OW76m8kwfpYuAyQjwGG+/dCorReaNvYr2p0J9D8j3UVaEokbBtP6FYLxvg0YCTa2WGX4GaN3jGZEL/gBxOgniZfLWfga7Ktm91In2hIviXAzZpAeL3WfKe8Wmj2wY1lJqRu4ilaBbjRoHn2G08YME1PtD+TvrzpA5kzXPg==~-1~-1~-1; nsit=R2A0xy2FpF0iSLTBLbtENzB4; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTczNDcwODA4MCwiZXhwIjoxNzM0NzE1MjgwfQ.NRuStChBBbNk1I5kJt2YQHLvVGVZ-Fz5MCkyCG_SHGI; bm_mi=1E432E84B4B13C73007EC7ACD573C24D~YAAQFf7UF71pP86TAQAA5LCo5BpoYrdRbeE9TDnfe/JWyKXjYDX525mFL9skf0D2kKjov7kJl9NNlIJYAa3KAY8IgGVNPNsRpVzPYMBJ85D5eYpov1gcwVSNLy15BKPYJG6eouUPi41LZpmo4XgpQL1C6/BCY/tWkd2LHUBzP+uVkFXGK09jfJg9O5z4RXQody2CiwZY1vQCAzPig2X5gsIomKzZDWRznzH2XV3KnW1MLLjxvSXcJYvYmGaRc9h8mfXCk3H8yU7kHkDqqpSGGTmdygUZp1XYEzKBY+P0AK6qefeUzgZviGLS6Abx6Q73dRC0uKSNeA8xJz6m2uPIRvBrG029s5/fxn5Iq1ag~1; bm_sz=1F93FAC96FAEEAFC2AF5051E8D5844FE~YAAQFf7UF79pP86TAQAA5LCo5Brb2wUGrbeaBpi5sYjF6hT2hQc7Dpt/kl/hz1pKhNE9wfsKfaRfv9dw8GY600fucMidKNsgRAPeI3Pq3VUa3CSGL7+fWuLWWEmEkdrYuF93SwdhjApCMLrN61ong5A+EWMg4SuQwvNVrOpViB49HpDtt3pMtiWFrQ11tPqGfD2WjbdJ3dd53WDH90rva/U6lvo5t7Ua8QvtXn52Ngu/KULIGbRO4ReeMmNXxUKgJLCnIDSOWZH9NOot1dnK8A+kWCs2I9LJeI/HxXL6R1ODojvL0BJZYRaUkmvrlnnpoHz35dn2ymOiL12yWPlybAb9Ol4IS0oPL4/jIJz4KMVN7JQG4ZsEmnY5uLd6IhJFHVBApDEByMlXghM11+6Xi2ar+gPvYp55LKNOvrCE~4277314~3225648; RT="z=1&dm=nseindia.com&si=9c11cbbe-166d-4fcc-b7e5-e5b5eb5536d7&ss=m4wlyfuv&sl=0&se=8c&tt=0&bcn=%2F%2F684d0d4b.akstat.io%2F"; ak_bmsc=2374F26B991857D22C99A6ED87914097~000000000000000000000000000000~YAAQFf7UF/JpP86TAQAAGbKo5BoN2KKMa6bjmRoOHmAHbyJrKZgGiZyKwY7OH/jQmkRPbnl/tnBqz38vnSMNtupd9OP5RRMVyEhvoshk/HJXFwhlGZe94DrGfB5YEI1rxcynr5spnJCEzZ4tkCHbXy9e8Kb1AFZDACx9A68GRDMX9kWeycnKyWlme6ebVZodLdv8oqLzUOiRo+G7gigqcsW7kIE8qr98JUxb7MozEssvi9DYSIiTPDSHoOmcrqJ1sV+7FEMOU6Y2gxhcab5hMk8tSTWs8s41e8/3vV49NfgQHp337cMrxWrn53LlJTW6hVdjQazVst5RD9HvfK2YtpXTmbW3yYXOHmMhg4tHzqpwAQ/we9IFpHjuqc0ZlYp/whV2NCID1g7oTeR/kIthVcR6t3MDM0uTl41k7plo9XBftMPj0EHQMqD3pnD+HnsqyXiod/Zvzrkp2HKqrC0dZy0szR/aZ0GcpiA7ow2bGKsQ0PWwx+ZOVIA3e+LuTeQzLz0CfcVC8E52vpotgN4U+dqEd2L1KA==; _ga_87M7PJ3R97=GS1.1.1734708080.28.1.1734708081.59.0.0; _ga_WM2NSQKJEK=GS1.1.1734708080.8.1.1734708081.0.0.0; bm_sv=5FC6DC0EF33832602833331AE01F11FE~YAAQFf7UFyJqP86TAQAAQbSo5BodsHhd2YJ0oLm+JW7IQIy80VupRYLgmmR3zW78uln2iXhCxrM6uGhVI5Xnsh1KXhJQsFcWzlWkpmBuKaiGj8u6k0N6m9Idf+so8vE8GEac4nKRlF/fGtbdvgYH7HMZG66yLsDNtOP617vZW9sLcu578xaVta/dkd7F9knltO80dWeAoJCox394AFTlqBfwhOvmWx0JF4jW/+jTCy1es+HTuqYpx8196bjUcAeCnhs=~1',
'priority': 'u=1, i',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',}

nse_oc_url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"
json_text = requests.get(url = nse_oc_url, headers = nse_headers, timeout = 20.0)
json_text.encoding='utf-8'
print(json_text)
print(json_text.headers.get('Content-Type'))


try:
    df = pd.DataFrame(json_text.json()['data'])
    #only keep necessary columns
    nifty_df = df.drop(['priority','ffmc','totalTradedVolume','stockIndClosePrice','totalTradedValue','nearWKH','nearWKL','chart365dPath','chart30dPath','chartTodayPath','series','meta'],axis=1)
    print(nifty_df)
    nifty_df.to_csv(r'C:\\Users\\vinay\\Documents\\VinayFirstAlgo\\DreamPortfolio\\DreamPortfolio\\instruments_csv\\' + f'nse_daily_data_{str_current_datetime}.csv', header=True, index=False)
except simplejson.errors.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")