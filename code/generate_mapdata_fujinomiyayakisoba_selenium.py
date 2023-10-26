# 富士宮焼きそば学会のサイトから、マップ用のデータを生成する

# インポート
import csv
# import requests
from bs4 import BeautifulSoup
import time
import random

# selenium用のインポート
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# デバッグ用
# from pprint import pprint

# 設定
## TODO: 2023-10-26 この部分は多数実行を考慮して最初は10件のみの取得にしています
SHOP_NUM = 10 # 取得する店舗数。Noneの場合はすべて取得する

# 定数
SITEURL = "https://umya-yakisoba.com/shop/"

# ブラウザのオプションを設定してwebdriverを用意 (headlessモード)
options = Options()
options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options)


def replace_text(text: str) -> str:
    """
    情報の中に入ってる文字から必要がない文字を取り除いたり置き換える。
    置き換える順番は辞書で書かれている順番になるので注意
    """
    replace_text_map = {
        "\n":"",
        " ":"", # 半角スペースを消す
        "\u3000": " ",
    }
    replaced_text = text
    for src, dst in replace_text_map.items():
        replaced_text = replaced_text.replace(src, dst)
    return replaced_text

def get_shopinfo_list(url: str) -> list[dict]:
    """
    該当URLから店舗情報を取得する。結果は辞書が入ったリストを返す。中身は店名, 詳細URL
    ページネーションが見つからず、サイト構造的に取得できない場合はNoneを返す
    """

    shoplist = []
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # これ以上ページがない場合の処理: サーバー側から404が返らないためページ構造で判定する
    if not soup.find('div', class_='pagination'):
        return None

    # ここではdiv,p-shopList > a にURLとその中にお店情報がまとまっているので、aタグから取り出す
    shopinfo_tags = soup.find('div', class_='p-shopList').find_all("a")
    
    for shopinfo_tag in shopinfo_tags:
        shopdata = {}
        # aタグの子要素となるdivは上から店名、住所、電話番号、定休日。
        # ここではurlと店名だけまとめたリストを作る
        shopdata['specurl'] = shopinfo_tag.get('href')
        # 店名にある余分な空白などを除去: relace_str関数
        shopdata['店名'] = replace_text(shopinfo_tag.find_all("div")[1].text)
        shoplist.append(shopdata)

    return shoplist

def random_sleep(a: int,b: int) -> None:
    """
    aからbまでのランダムな時間を待つ。引数は秒数
    args:
        a: int
        b: int
    """
    time.sleep(random.randint(a,b))

# ページネーションのページ数。2から始める
pagenum = 2 
# 学会の一覧から、店舗名と詳細情報用のURLを取得する。マップのセットにしておく
shopinfo_list = []

# ページの中にある店舗一覧の中から、店舗名と詳細URLを取得
# 最初のページを試す
print("page.1 処理中...")
shopinfo_list.extend(get_shopinfo_list(SITEURL))


# 2ページ目以降、ページネーションはすでに決まってるので、そのままループで回す
while True:
    print(f"page.{pagenum} 処理中...")
    pageurl = SITEURL + f"page/{pagenum}/" # ページネーションのURL -> https://umya-yakisoba.com/shop/page/2/

    # ページが取得できなかったらループを抜ける: エラー処理としては緩いです
    if get_shopinfo_list(pageurl) is None:
        break
    shopinfo_list.extend(get_shopinfo_list(pageurl))

    # 次のページへアクセスするためにページ数を増やす
    pagenum =  pagenum + 1

    # ランダム時間待つ
    random_sleep(1,5)

# SHOP_NUMが設定されていたら、その数だけ店舗情報を取得する
if SHOP_NUM:
    shopinfo_list = shopinfo_list[0:SHOP_NUM]

print("店舗情報取得完了")
print("店舗情報詳細取得中...")

# 詳細URLからさらに詳細情報を取得する
for shopinfo in shopinfo_list:
    # URLから店舗情報を取得
    driver.get(shopinfo['specurl'])
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # dl.p-shopDetails > dt/dd構造でdtが項目、ddが値になっている。これを辞書形式にする
    shopspecs = {}
    for dt, dd in zip(soup.find('dl', class_='p-shopDetails').find_all('dt'), 
                      soup.find('dl', class_='p-shopDetails').find_all('dd')):
        # 値に 改行や空白文字があるので取り除く
        shopspecs[dt.text] = replace_text(dd.text)

    # 店舗情報をマップ情報に追加
    shopinfo.update(shopspecs)

    # ランダム時間待つ
    random_sleep(1,5)

print("スクレイピング処理完了")
# pprint(shopinfo_list)

print("CSVファイルに書き出し中...")
# mapinfo_listをCSVファイルに書き出してみる。辞書内の値はすべて書き出す
with open('mapdata.csv', 'w', newline='') as csvfile:
    # お店の詳細情報の各項目:辞書のキー が部分的にあったりなかったりしたので
    # 全ての辞書のキーから全ての項目をカバーしたリストを生成する
    # またソートをして項目の順番を揃える
    fieldnames = sorted(list(set().union(*shopinfo_list)))

    # CSVファイルに書き出す
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for shopinfo in shopinfo_list:
        writer.writerow(shopinfo)
    print("CSVファイルへの書き出し完了")
