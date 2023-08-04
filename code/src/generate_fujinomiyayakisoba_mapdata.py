# 富士宮焼きそば学会のサイトから、マップ用のデータを生成する
# メモ

# * ここでは富士宮焼きそばのまっぷを作るためのデータを生成する
# * ノウハウ的なことを伝えることにしてみる。
# * データの取得と出力の間の前処理が結構大変なのよね。ここがあることがわかるとデータを作るという作業に馴染めると思う。
# * 言いたいテーマはそこでいいかな。


# インポート
import csv
import requests
from bs4 import BeautifulSoup

# デバッグ用
from pprint import pprint

siteurl = "https://umya-yakisoba.com/shop/"
pagenum = 2 # ページネーションのページ数。2から始める

def replace_str(text: str) -> str:
    """
    情報の中に入ってる文字から必要がない文字を取り除いたり置き換える。置き換える順番は辞書で書かれている順番
    """
    nouse_str_map = {
        "\n":"",
        " ":"", # 半角スペースを消す
        "\u3000": " ",
    }
    replaced_text = text
    for key,val in nouse_str_map.items():
        replaced_text = replaced_text.replace(key,val)
    return replaced_text

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
        mapdata = {}
        # divは上から店名、住所、電話番号、定休日。
        # ここではurlと店名だけまとめたリストを作る
        mapdata['specurl'] = shopinfo_tag.get('href')
        mapdata['店名'] = replace_str(shopinfo_tag.find_all("div")[1].text)
        shoplist.append(mapdata)

    return shoplist


# 学会の一覧から、店舗名と詳細情報用のURLを取得する。マップのセットにしておく
mapinfo_list = []

# ページの中にある店舗一覧の中から、店舗名と詳細URLを取得
# 最初のページを試す
print("page.1")
mapinfo_list.extend(get_shopinfo_list(siteurl))

# 2ページ目以降、ページネーションはすでに決まってるので、そのままループで回す
# while True:
#     print(f"page.{pagenum}")
#     pageurl = siteurl + f"page/{pagenum}/" # ページネーションのURL -> https://umya-yakisoba.com/shop/page/2/

#     if get_shopinfo_list(pageurl) is None:
#         break
#     mapinfo_list.extend(get_shopinfo_list(pageurl))

#     # ページネーション処理
#     pagenum =  pagenum + 1

# pprint(mapinfo_list)

# とりあえず絞って詳細収集する
mapinfo_list = mapinfo_list[0:10]

# 詳細URLからさらに詳細情報を取得する
for mapinfo in mapinfo_list:
    # URLから店舗情報を取得
    res = requests.get(mapinfo['specurl'])
    soup = BeautifulSoup(res.text, 'html.parser')

    # dl.p-shopDetails > dt/dd構造でdtが項目、ddが値になっている。これを辞書形式にする
    shopspecs = {}
    for dt, dd in zip(soup.find('dl', class_='p-shopDetails').find_all('dt'), 
                      soup.find('dl', class_='p-shopDetails').find_all('dd')):
        # 値に 改行や空白文字があるので取り除く
        shopspecs[dt.text] = replace_str(dd.text)

    # 店舗情報をマップ情報に追加
    mapinfo.update(shopspecs)

pprint(mapinfo_list)

# mapinfo_listをCSVファイルに書き出してみる。辞書内の値はすべて書き出す
with open('mapdata.csv', 'w', newline='') as csvfile:
    # フィールド名がまばらだったので、生成する
    # すべてmapinfoからフィールド名を取得してsetで重複を取り除いて、リストに戻す
    fieldnames = list(set().union(*mapinfo_list))

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for mapinfo in mapinfo_list:
        writer.writerow(mapinfo)

