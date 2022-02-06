import os
import json
import requests as rq

class HotpepperManager(object):
    def __init__(self, api_key) -> None:
        self.API_KEY = api_key
        self.BASE_URL = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

    def search_shop_list(self, lat:str, lng:str):
        """グルメサーチAPIを使用して店舗情報を取得する"""

        query = {
            "key": self.API_KEY,
            "lat": lat,
            "lng": lng,
            "range": 3,
            "format": "json"
        }

        # APIリクエスト
        res = rq.get(self.BASE_URL, query)
        # JSON→辞書形式
        # res_dict = json.loads(res.text)
        res_dict = json.loads(res.text)["results"]["shop"]

        return res_dict[0]
        

    def search(self):
        pass

if __name__ == "__main__":
    API_KEY = os.environ.get("HOTPEPPER_API_KEY")

    hm = HotpepperManager(API_KEY)
    hm.search_shop_list("35.6895014", "139.6917337")
