import requests

def ip_to_geoLocation(ip: str) -> dict:
    '''
    Function：解析ip为地理省份城市信息
    Return: 返回包含省份(regionName)、城市(city)、经纬度等信息的字典
    '''
    se = requests.Session()
    resp = se.get(f'http://ip-api.com/json/{ip}?lang=zh-CN')
    resp_dict: dict = resp.json()

    return resp_dict

