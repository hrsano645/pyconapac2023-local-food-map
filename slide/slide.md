---
marp: true
paginate: true
---

# ご当地グルメマップを作ろう  

# Lets create! Local Food Map

### PyCon APAC 2023 Day2

Hiroshi Sano / 佐野浩士

![width:200px](./images/pyconapac2023_logo.png)

---

## Agenda

* トークのモチベーション
* 情報を集めよう: どの情報を使うか
* マップデータを作ろう: 情報収集をアウトプット
* 利用先を考えよう: サービスと連携しよう

---

## Today's Document

付録含めてすでに公開されています。

* GitHub: Starくれー！
  <https://github.com/hrsano645/pyconapac2023-local-food-map>

* スライド
  <https://github.com/hrsano645/pyconapac2023-local-food-map/slide/slide.pdf>

あとでトライしたい方は参考にしてみてください。

---

## Self Infroduction

Hiroshi Sano(佐野浩士) [@hrs_sano645](https://twitter.com/hrs_sano645)

* 🏢: [株式会社佐野設計事務所](https://sano-design.info) CEO
* 🐍: PyCon mini Shizuoka Stuff
  * Shizuoka.py / Unagi.py / PythonSuruga
* CivicTech, [Startup Weekend Oganizatior](https://swfuji.doorkeeper.jp)
* Hobby: Camp🏕️,DIY⚒️,IoT💡

![w:200px](./images/sns-logo.jpg)![w:300px](./images/shizuokaLogo.png) ![w:200px](https://lh3.googleusercontent.com/pw/AIL4fc9DDT9ootdGiDNZiGUybbHE5WRnm68hFp6XknmZc2lVttIBKJ180GVq0NE2qtcGRbx8OBVAak3E4qHa7H5iXw8gtQqkY4l6tWrFkIHUA96q1jcqE2_f) ![w:200px](https://lh3.googleusercontent.com/pw/AIL4fc_3zxLYLoa5SSL_apqpJ3WCY9BRMfXRL4jUYaYouX3MvqiMU5eSCi8be6eQIvboRzgNZ3ZvdZAIET40tJD7I4y8dSHF6UByo-u8jXhLFFGv5rAw_kZU)

---

![bg](./images/sano-design_info.png)

<!-- 

* 株式会社佐野設計事務所は主に自動車プレス金型の機械設計を行う事務所です。
* 3D CADを扱った設計や、金型関連、製品形状の3Dモデリングを扱っております。
* 設計データをデジタルで扱うこともあり、様々な業務の効率化をPython＋クラウドサービスを組み合わせて、実現しています。
* 製造業とデジタル化で取り組まれていたり、ご興味ある方がいましたら、後ほどのパーティでぜひお話ししましょう！

-->

---

## トークのモチベーション

* ご当地グルメを**情報収集してマップを作りましょう！** 食べに行きましょう！
  * ご当地グルメ=B級グルメのこと
* PyCampを終えた人に: **Pythonでデータを集めて作り利用するプロセス**   を学べます
  * 初学者向けの内容です
  * 話すこと: トークお題をPythonで実装する過程
  * 話さないこと: Pythonの基礎や文法の解説

---

## PyCamp:Python Boot Campとは

* 日本全国で開催されているPythonの学習プログラム
* 半日をかけて、Pythonの基礎を学び、簡単なプログラムを作る
  * 専用テキストを元に講師とTAがサポート

![h:300px](./images/pycamp-text.png)

このトークはその続きからトライできるコンテンツを目指して作りました

---

## PyCampの様子

<!-- ここに3枚の静岡開催の写真を載せる -->
![h:250px](https://lh3.googleusercontent.com/pw/AIL4fc-QihRkRpnkffJ9b1pmbmM6J4Jc4hkDXCleYASV-peLtXU9USqbL41kQjl85yDJAjUrSDFe0yDxO-ygY-U0TlYC1vhW7z5dmeOFBok8Z1wA9mXsbrIR) ![h:250px](https://lh3.googleusercontent.com/pw/AIL4fc9_J_x8gcqjZ828PuiB3sVh7FjhZW8ZTWXSzBOZSZxTFh9dnbBIvTU2KsnQGH7iZacfkPJix4lsezINDWNERljbRgfUPFjAKFkDFgtuXI1OzJegQRhy) ![h:250px](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjS_cCQlBadAUmQnxucUD5NjwxcSqAJzILkL7ng1PEgrKqPh8mvT8KkHd1XueX40o_DydsBO6iNB8K3HWdOnXb0csUkMQ3th9uBbFJ9DkB4qEQgY6X43vM9s0ieoYgsitSTU-6VdXvxaGvfMyVH1ZRk5WALgXjR7bHXY4SFmOZo0x5_hhSEHpfe7h68/s5472/IMG_5991.jpg)

<!-- _footer: 静岡県3回目の様子 -->

---

## 今回のお題: 本題のご当地グルメ

---

## 富士宮焼きそば

![h:500px](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Fujinomiya-yakisoba.jpg/800px-Fujinomiya-yakisoba.jpg)

<!-- _footer: しんかわな, CC BY 3.0 <https://creativecommons.org/licenses/by/3.0>, ウィキメディア・コモンズ経由 -->

---

* 主に静岡の富士宮市周辺で食べられる焼きそば
* 麺は富士宮周辺でしか手に入らない。まさにローカルフード
* B級グルメグランプリは殿堂入り
* 最近NYで開催されたコナモングランプリで優勝した

![h:300px](./images/fujinomiyashi-map2.png) ![h:300px](https://lh3.googleusercontent.com/pw/AIL4fc_qzyqjAu3-1DV-HK-b02ln329d9Rsp45D1VYSlzc6Qpkk73NwvzCEXCLjjgXIGrCDq2pRNobz3dEnzgNjZHlcgEbmuMMV7cyksEf2O7dvMF2GHZ9zD)
<!-- ここに、どの地点で食べられるか地図を入れる、材料がまとまった絵を載せる -->

<!-- _footer: 地元の人は、多分月に数回は食べてる -->

---

ところで、みなさん

---

もう食べたくなりましたね？🤤

<!-- _footer: このあとはパーティ🎉ですし、お腹空きましたね🤤 -->

---

**富士宮焼きそばマップを作りましょう！**

---

## 今回のトークで目指すこと

1. お店情報を探してWEBスクレイピング
2. データを整形 -> CSVファイルにする
3. Googleマイマップで呼び出す

---

## 今回のトークで目指すこと

![bg left:40%](./images/programing-flow.png)

1. お店情報を探してWEBスクレイピング
2. データを整形 -> CSVファイルにする
3. Googleマイマップで呼び出す

↓

1. データを読む/取り込む
2. データを加工/出力する
3. データを使う/活用する

この流れで説明します。

---

## ご当地グルメの情報はどこにあるか

* 地域の情報を収集
* **そこの情報は機械可読性があるか**
  * 大体が紙ベースが多い...（画像識別の手段は使える）

観光情報を探ってみると...

* 市役所で紹介されていたり
* 観光協会で紹介されていたり
* ご当地グルメの公式サイト（よく〇〇学会とも言われる）

<!-- _footer: グルメ情報サイトを見たらそこで試合終了ですよ -->

---

今回は、富士宮焼きそば学会の公式サイトを例にしています。

<https://umya-yakisoba.com/shop/>

<!-- _footer: 富士宮焼きそば学会の公式サイトを見せます -->

---

## 1. データを読む/取得する

![bg left:40%](./images/programing-flow.png)

* **WEBスクレイピングで収集する**
* [付録]画像識別で加工を試みる

<br>

機械可読性はどちらも微妙
WEBスクレイピングはまだやりやすい

---

## ⚠️WEBスクレイピングの注意点⚠️

**※スクレイピング対象のサイトへ多数のアクセスはしないように注意**

* 単純に迷惑かけがち、トラブルになりがち
* 作ってる最中にエラーでアクセスが止まらないとか
* 試すときは少し時間を置きながらアクセスしましょう
  * ランダム時間置いてみるとか
  * 回数リミットをつけて待つようにする
  * サイトポリシーがあれば従う

---

## 利用するライブラリ

* requests: HTTPアクセス→情報取得（今回はHTML）
* BeautifulSoup4: HTML（マークアップ言語）解析と抽出

```bash
pip install requests
pip install beautifulesoup4
```

※:スライドのコードは説明向けです。そのままだと動かないこともあります
資料のリポジトリから動作するスクリプトをDL可能です。

---

<!-- TODO: 2023-10-08 挿絵を入れ替え: divのお店名が展開されている状態、もう少し横長でよし -->

サイトの構造を見てみましょう

この構造からBeautifulSoup4を使って必要な情報を取り出します。

![h:500px](./images/gakkai_1.png)

---

構造の中にあるタグから必要な情報を取得する

```python
import requests
from bs4 import BeautifulSoup

url = "https://umya-yakisoba.com/shop/"
shopinfo_list = []
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')


# ここではdiv.p-shopList > a にURLとその中にお店情報がまとまっているので、aタグから取り出す
shopinfo_tags = soup.find('div', class_='p-shopList').find_all("a")
```

---

<!-- 画像: どこの構造を取り出しているかの画像を載せる -->

<!-- ![bg:40%]() -->

aタグの下にあるそれぞれのタグから必要な情報を取得する

```python

for shopinfo_tag in shopinfo_tags:
    shopdata = {}
    # divは上から店名、住所、電話番号、定休日。
    # ここではurlと店名だけまとめたリストを作る
    shopdata['specurl'] = shopinfo_tag.get('href')
    shopdata['店名'] = replace_str(shopinfo_tag.find_all("div")[1].text)
    
    shopinfo_list.append(shopdata)

```

※ replace_str関数は店名に出てくる空白文字を置き換えたりする独自に作った関数（後述します）

---

お店の詳細URL, 店名を手に入れた！

```python
>>> shopinfo_list
[{'specurl': 'https://umya-yakisoba.com/shop/3776/', '店名': 'お好焼 あき'},
 {'specurl': 'https://umya-yakisoba.com/shop/3777/', '店名': 'あさ家'},
 {'specurl': 'https://umya-yakisoba.com/shop/3774/', '店名': 'あるばとろす'},
 {'specurl': 'https://umya-yakisoba.com/shop/3616/', '店名': 'いっぷく亭'},
...
]
```

---

収集した詳細URLのリストを使って、お店情報収集

![h:500px](./images/gakkai_2.png)

`dt`と`dd`タグは記述リスト、説明リストと呼ばれるHTMLタグ

---

```python
for shopinfo in shopinfo_list:
    # URLから店舗情報を取得
    res = requests.get(shopinfo['specurl'])
    soup = BeautifulSoup(res.text, 'html.parser')

    # dl.p-shopDetails > dt/dd構造でdtが項目、ddが値になっている。これを辞書形式にする
    shopspecs = {}
    for dt, dd in zip(
      soup.find('dl', class_='p-shopDetails').find_all('dt'),
      soup.find('dl', class_='p-shopDetails').find_all('dd')
    ):
        # 値に 改行や空白文字があるので取り除く
        shopspecs[dt.text] = replace_str(dd.text)

    # 店舗情報をマップ情報に追加
    shopinfo.update(shopspecs)
    # INFO:ここにランダム待機時間があるとよさそう
```

---

最終的にできるデータ

```python
>>> from pprint import pprint
>>> pprint(shopinfo_list)
[{'TEL': '0544-27-0004',
  'specurl': 'https://umya-yakisoba.com/shop/3776/',
  'お店名ふりがな': 'あき',
  'エリア': 'まちなか',
  '住所': '富士宮市野中東町112-1',
  '受入人数': '12',
  '営業時間': '10:00－21:00',
  '地図': 'B6',
  '定休日': '火曜日',
  '店名': 'お好焼 あき',
  '料金目安': '350～600円',
  '業種': '飲食店',
  '焼き方': 'お店',
  '調査員おすすめメニュー': 'キムチとチーズ入り',
  '調査員が見た特徴': 'キャベツとネギが多めに入っている',
  '駐車場': '4'},
  # 以下お店情報の辞書が続いて入る
  # ...
]
```

---

## 上のコードの注意点

※: サイト上に見えない文字があることがあります → 文字列置換をしましょう

※: この例を使って、何度もWEBスクレイピングはしないようにしましょう。
randomモジュールやtimeモジュールを組み合わせてランダム時間待機します

※: この例ではサイトのページネーションに対応していません
ページネーションについては資料のコードで対応しています

---

店名にある空白などを取り除きます。

```python
def replace_str(text: str) -> str:
  
    replace_str_map = {
        # 置き換え対象文字列:置き換え先の文字列
        "\n":"", 
        "\u3000": " ",
    }
    replaced_text = text
    for key,val in replace_str_map.items():
        replaced_text = replaced_text.replace(key,val)
    return replaced_text

# 例:
print(replace_str("お好焼\u3000さの"))
# お好焼 さの
```

---

ランダム時間待機できる関数の例

```python
import random
from time import sleep

def random_sleep(a: int,b: int) -> None:
    """
    aからbまでのランダムな秒数を待つ
    
    """
    time.sleep(random.randint(a,b))

# ランダム時間を待てるようにする
random_sleep(2, 5)
```

---

## 2.データを加工/出力する

![bg left:40%](./images/programing-flow.png)

マップのもとになるデータを作成します

* **情報を整理して表形式ファイルで書き出す**
* [付録]地理情報を集める

---

## 情報を整理

どのフォーマットで書き出すか？

よくある地理データ構造、フォーマット形式

* **CSV（区切り表形式、汎用性高）**
* GeoJSON（WEB APIで広く流通しているJSON形式の地理情報向け）
* KML（XML形式）

<!-- _footer: ※どのような使い方にもよります。他にもあったら教えてください -->

---

CSVライブラリを使って書き出せます

`csv.DictWriter`を使うと辞書のキーを使って列見出しを用意できる

```python
with open('mapdata.csv', 'w', newline='') as csvfile:
    # 今回の例では、辞書のキー（お店の詳細情報の各項目）が部分的にあったりなかったりしたので
    # 全ての辞書のキーから全ての項目をカバーしたリストを生成する
    fieldnames = list(set().union(*shopinfo_list)

    writer = csv.DictWriter(csvfile, fidnames=fieldnames)
    writer.writeheader()
    for shopinfo in shopinfo_list:
        writer.writerow(shopinfo)
```

---

出力できたCSVファイル

![h:300px](./images/csv1.png)![h:300px](./images/csv2.png)

---

## データを使う/活用する

旅行中に使うためのツールとして

* **巨人の肩に乗る: Googleマイマップで使おう**
* [付録]ポータブルに扱う: 印刷をする
* [付録]専用のWEBアプリを作ろう

Googleマイマップで使おう

* Googleが提供するマップのピンや経路をオリジナルで作成できるサービス
* アカウントに紐づいて、スマホ版Googleマップでも表示可能

---

## 扱い方

`https://www.google.com/maps/d/` へアクセスして利用します。

「新しい地図を作成」ボタンを押す

![h:350px](./images/google_mymap1.png)

---

新規レイヤーへCSVファイルをインポートします

![h:450px](./images/google_mymap2.png)

---

マップへのポイントは住所を使います

![h:450px](./images/google_mymap3.png)

---

ポイントした部分への簡易説明（マーカー）を入れる。

今回は店名にしました。

![h:450px](./images/google_mymap4.png)

---

マッピングされました🎉

![h:450px](./images/google_mymap5.png)

---

スマホで見ることもできます！📱

![h:400px](./images/google_mymap6.png)

---

## マッピングのそのほか選択肢

今回はGoogleマップを利用しましたが、推奨しているわけではなくて
データを作るといろんなサービスと連携できることをお伝えしました。

※: オリジナルのマップを作るサービスは他にも多数あります。一例を載せておきます。
※: それぞれ特徴や無料有料とあるので、使いやすいものを探すと良いと思います

* OpenStreetMap uMap: <https://umap.openstreetmap.fr/ja/>
* proxi: <https://www.proxi.co/>
* [日本向け]国土地理院: <https://maps.gsi.go.jp/>
* etc...

---

## トークのまとめ

---

![bg left:40%](./images/programing-flow.png)

## 今回のトークで目指すこと

1. お店情報をWEBスクレイピング
2. 表形式に整形 -> CSVファイル
3. Googleマイマップで呼び出す

↓

1. データを読む/取り込む
2. データを加工/出力する
3. データを使う/活用する

---

今日学んだことを応用すると

* WEBスクレイピングでデータ収集 -> 世の中のWEBサイトの収集
  **※扱いには気をつけましょう**
  * WEB APIを扱えると収集や操作はもっと楽
* データの書き出し: CSV以外にもjson, xlsx, etc....
* 他のサービスへの連携:データベースに入れたりもできますよね

---

プログラミングでもっとも行われる行為

* **どこから** データを取り出すか
* **どこへ** データを書き出すか

<!-- _footer: もちろん他にもありますが、概念として最終的にデータ/ファイルを扱うことが多いと思います -->
---

* **どこから** データを取り出すか
  * データベースから取り出す
  * データ分析で現実の統計データを使う
  * センサーデータで現実環境を使う
* **どこへ** データを書き出すか
  * データ分析でサービス改善
  * 得られたデータを使って業務工程改善

---

* **どこから** データを取り出すか
  * データベースから取り出す -> データベースと接続するライブラリ
  * データ分析で現実の統計データを使う -> オープンデータ API/ファイル
  * センサーデータで現実環境を使う -> ハードウェア操作のライブラリ
* **どこへ** データを書き出すか
  * データ分析でサービス改善 -> 可視化して統計処理
  * 得られたデータを使って業務工程改善 -> オートメーション, 他システム連携

<!-- _footer: データの流れを意識すると、作りたいプログラムの流れも理解しやすい -->

---

## 最後に伝えたいこと

PyCampやPythonの基礎を学んだ方の一歩先として！

自分が使いたい、利用したい、ものやことでトライしましょう！

それたできたら、とても楽しいし感動します。オススメです！

---

**Happy Hacking!!**

**and, Have a nice trip!!**

---

## 付録

---

今回扱わなかった他の方法については、またどこかで解説できたらと思います

* WEBスクレイピングしづらいサイトもカバーする
  * selenium + headless chrome
* 画像識別でお店情報を収集する
  * OCR, Googleなど
* 緯度経度を収集
  * 世界: Google?
  * 日本: 東大CSIS
* 印刷物を作る -> テンプレートエンジンで印刷しやすいHTMLを生成
* fletで自分専用のマップアプリを作る

---

## WEBスクレイピング: Seleniumの例

* 動的な（javascriptなど利用した）サイトはrequestsで対応が難しいことがあります
* 本物のブラウザ + ブラウザ自動操作ツール(selenium)を使った例も載せておきます

-> url

---

## 画像識別

結構難しい分野（ちょっと自信ない）

* Google Cloud Vision
  * -> url

---

## 位置情報

* 世界: Google Maps Platform ->
  <https://developers.google.com/maps/documentation/geocoding/overview?hl=ja>
  * -> url

* 日本: 東大CSIS -> jageocoder
  <https://github.com/t-sagara/jageocoder>
  * 無料で利用できる（リクエスト数は少なめがよし
  * -> url

---

## 印刷用マップを作ってみる

印刷用のHTMLファイルを作って印刷してみる

* Mapboxで概要と詳細の地図を用意
* お店の情報をテーブルで埋め込む
* 印刷用にCSSで調整する

-> url

---

## モバイル向けのWEBアプリ

<!-- 実際に作成してみる -->

実験的な扱いです。うまく動かなければ...

* fletを使って作ってみました
* staticなページでWASMとして埋め込んで作ってみる
  * <https://flet.dev/docs/guides/python/publishing-static-website/>
* ※サイト自体の公開はしません

-> url
