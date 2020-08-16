import requests
url='http://120.78.128.25:8766/futureloan/member/login'
data={"mobile_phone":"15815541763","pwd":"lemon123456"}
header={'X-Lemonban-Media-Type':'lemonban.v2'}
def qingqiu(url,data,header,method='post'):
    if method=='get':
        response=requests.get(url=url,json=data,headers=header)
    else:
        response = requests.post(url=url, json=data, headers=header)
    return response.json()
if __name__ == '__main__':

    response=qingqiu(url,data,header)