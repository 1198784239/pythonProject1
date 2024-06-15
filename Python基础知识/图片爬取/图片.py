import requests

url = 'https://www.vcg.com/creative-illustration/tiantang/'
response = requests.get(url)
print(response.text)