# 富士宮焼きそば学会のサイトから、マップ用のデータを生成する

# インポート
import requests
from bs4 import BeautifulSoup


siteurl = "https://umya-yakisoba.com/shop/"
pagenum = 2 # ページネーションのページ数。2から始める

def get_shopinfo_list(url) -> list[dict]:
    """
    該当URLからshoplistを取得する。結果は辞書が入ったリストを返す
    ページネーションが見つからず、サイト構造的に取得できない場合はNoneを返す
    """

    shoplist = []
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    # これ以上ページがない場合。404が帰らないのでページ構造で判定する
    if not soup.find('div', class_='pagination') :
        return None

    # ここではdiv,p-shopList > a にURLとその中にお店情報がまとまっているので、aタグから取り出す
    shopinfo_tags = soup.find('div', class_='p-shopList').find_all("a")
    
    for shopinfo_tag in shopinfo_tags:
        # divは上から、店名、住所、電話番号、定休日。ここではurlと店名だけまとめたリストを作る
        mapdata = {}
        mapdata['specurl'] = shopinfo_tag.get('href')
        mapdata['店名'] = shopinfo_tag.find_all("div")[1].text
        shoplist.append(mapdata)

    return shoplist


# 学会の一覧から、店舗名と詳細情報用のURLを取得する。マップのセットにしておく
mapinfo_list = []

# 最初のページを試す
print("page.1")
res = requests.get(siteurl)

# ページの中にある店舗一覧の部分を取得
# 店舗一覧の中から、店舗名と詳細URLを取得
mapinfo_list.extend(get_shopinfo_list(siteurl))


# ページネーションはすでに決まってるので、そのままループで回す
while True:
    print(f"page.{pagenum}")
    pageurl = siteurl + f"page/{pagenum}/" # ページネーションのURL -> https://umya-yakisoba.com/shop/page/2/

    if get_shopinfo_list(pageurl) is None:
        break
    mapinfo_list.extend(get_shopinfo_list(pageurl))

    # ページネーション処理
    pagenum =  pagenum + 1

from pprint import pprint

pprint(mapinfo_list)

# 詳細URLからさらに詳細情報を取得する
