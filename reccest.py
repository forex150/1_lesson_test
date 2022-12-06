import requests

url = 'https://eodx6hp80fxuh64.m.pipedream.net'
json = {
    'month':'May',
    'resulr':'1:0',
    'fond':'manchester'
}
respone = requests.post(url,params=json)
print(respone.json())

url2 = 'http://httpbin.org/'
params = {
    'id' : [1,2,3,4,5],
}
respone = requests.get(url2,params=params)
print(respone.json)

#www.chrome.com/napp?id=12&name=Bob