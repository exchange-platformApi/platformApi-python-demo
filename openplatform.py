import hmac
import json
import requests
import time
import hashlib

# 输入的您的apiKey和secretKey
# Enter your apiKey and secretKey
appkey = 'xxx'
secret = 'xxx'

#拼接参数
#Stitching parameters
def preHash(map,secretKey):
    str = "";
    for key in map.keys():
        str += key + map[key];
    return str+secretKey

#生成签名
#To generate the signature
def toString(map,secretKey):
    sign = preHash(map, secretKey)
    print("拼接==="+sign)
    print("Joining together==="+sign)
    return sign

if __name__ == '__main__':

    #url
    url = "https://service.xxx.com/platformapi/chainup/open/auth/token"
    timestamp = str(round(time.time()))

    #拼接参数的字典
    #A dictionary of concatenated parameters
    map = {'appKey': "xxx", 'symbol': 'ltcbtc', 'time': timestamp}

    param = toString(map, secret)
    md5_machine = hashlib.md5()
    md5_machine.update(param.encode(encoding='utf-8'))
    sign = md5_machine.hexdigest()
    print('MD5加密后为 ：' + sign)
    print('MD5 encryption ：' + sign)


    #请求体
    #body
    body = json.dumps({"symbol": "ltcbtc", "appKey": appkey, "sign": sign, "time": timestamp})

    # 构造Headers
    # Construct Headers
    postHeaders = {
        'Content-Type': 'application/json',
    }
    response = requests.post(url=url, headers=postHeaders, data=body)
    print(response.text.encode('utf8'))



