import http.client
import hashlib
import urllib
import random
import json

def translate(q):
    appid = '' # Your baidu translation API Appid
    secretKey = '' # Your baidu translation API Key

    httpClient = None
    myurl = '/api/trans/vip/translate'

    fromLang = 'jp'
    toLang = 'zh'
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
    salt) + '&sign=' + sign

    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)

    response = httpClient.getresponse()
    result_all = response.read().decode("utf-8")
    result = json.loads(result_all)

    return result['trans_result'][0]['dst']
