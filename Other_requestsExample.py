import json
import requests
from requests_ntlm import HttpNtlmAuth
import smtplib


url = 'https://ppp.slb.com/Shared/iFindIntegration/ValidateUWIWellID'

payload = {'UWI': '42311359730000', 'WellID': '0631549827'}

msg = {}
try:
	response = requests.post(url, json = payload, auth = HttpNtlmAuth('DIR\\i-FindApplication','Sugar#110*2017Q4'), verify=False)
	print response.status_code
	print response.text

except Exception, ex:
    print ex
