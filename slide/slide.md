---
marp: true
paginate: true
backgroundColor: #fbf9f4
---

# ご当地グルメマップを作ろう  

# Let's make! Local Food Map

### PyCon APAC 2023 Day2

Hiroshi Sano / 佐野浩士

![width:300px](./images/pyconapac2023_logo.png)

---

# Today's Document

本日の資料は公開されています

* スライド: Speaker Deck
  <URL載せ替えます>
  
* GitHubリポジトリ: コードとスライド
  <https://github.com/hrsano645/pyconapac2023-local-food-map>

<!-- _footer: GitHubのStarくれー🦖👍！！ -->

---

# Self Infroduction

Hiroshi Sano（佐野浩士）[@hrs_sano645](https://twitter.com/hrs_sano645)

* 🗺️: Shizuoka, Eastern part🗻
* 🏢: 株式会社佐野設計事務所 CEO
* 👥🤝
  * 🐍: PyCon mini Shizuoka Stuff / Shizuoka.py / Unagi.py / Python駿河
  * CivicTech, Startup Weekend Organizer
* Hobby: Camp🏕️,DIY⚒️,IoT💡

![w:180px](./images/sns-logo.jpg)![w:360px](./images/shizuokaLogo.png) ![w:180px](https://lh3.googleusercontent.com/pw/AIL4fc9DDT9ootdGiDNZiGUybbHE5WRnm68hFp6XknmZc2lVttIBKJ180GVq0NE2qtcGRbx8OBVAak3E4qHa7H5iXw8gtQqkY4l6tWrFkIHUA96q1jcqE2_f) ![w:180px](https://lh3.googleusercontent.com/pw/AIL4fc_3zxLYLoa5SSL_apqpJ3WCY9BRMfXRL4jUYaYouX3MvqiMU5eSCi8be6eQIvboRzgNZ3ZvdZAIET40tJD7I4y8dSHF6UByo-u8jXhLFFGv5rAw_kZU)

---

![bg](./images/sano-design_info.png)

<!-- 

* 株式会社佐野設計事務所は自動車プレス金型という、金型という機械を設計する事務所です。3D CADを使い設計、また他業界含む製品の3Dモデリングを扱っております。
* こういった設計データはデジタルデータになります。データを使い関連業務の改善に、Python＋クラウドサービスなどを組み合わせて実現しています。
* 製造業なのですがデジタル化で取り組んでいます。同じように取り組まれている方やご興味ある方がいましたら、後ほどのパーティでぜひ意見交換できたらと思います。
* もちろん静岡のPythonコミュニティとしても参加していますので、コミュニティスタッフとしてもお気軽にお声がけください！
-->

---

# Agenda

* トークのモチベーション
* 今回のトークでできること

1. お店情報をデータにする: WEBスクレイピング
2. データを整形をする: CSVファイルにする
3. データを使ってみる: Googleマイマップで呼び出す

* まとめ

---

# トークのモチベーション

* **ご当地グルメを情報収集してマップを作りましょう！**
  * ご当地グルメ=B級グルメのこと
  * とあるご当地グルメを例にしています
* PyCampを終えた人に:
  **Pythonでデータを集める、作る、利用する**プロセスを学べます
  * 話すこと: トークお題をPythonで実装する過程
  * 話さないこと: Pythonの基礎や文法の解説

---

## PyCamp:Python Boot Campとは

* 日本全国で開催されているPythonのチュートリアルイベント
  * 一般社団法人PyCon JP Associationが主催
* 半日でPythonの基礎を学び、簡単なプログラムを作る
  * 専用テキストを元に講師、TAがサポート

![h:250px](./images/pycamp-text.png) ![h:200px](https://lh3.googleusercontent.com/pw/AIL4fc9_J_x8gcqjZ828PuiB3sVh7FjhZW8ZTWXSzBOZSZxTFh9dnbBIvTU2KsnQGH7iZacfkPJix4lsezINDWNERljbRgfUPFjAKFkDFgtuXI1OzJegQRhy) ![h:200px](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjS_cCQlBadAUmQnxucUD5NjwxcSqAJzILkL7ng1PEgrKqPh8mvT8KkHd1XueX40o_DydsBO6iNB8K3HWdOnXb0csUkMQ3th9uBbFJ9DkB4qEQgY6X43vM9s0ieoYgsitSTU-6VdXvxaGvfMyVH1ZRk5WALgXjR7bHXY4SFmOZo0x5_hhSEHpfe7h68/s5472/IMG_5991.jpg)

PyCampを終えた方の次にチャレンジできるコンテンツを目指して作りました

<!-- _footer: 写真は静岡県3回目の様子 -->

---

## 今回のお題: 本題のご当地グルメ

![h:500px](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Fujinomiya-yakisoba.jpg/800px-Fujinomiya-yakisoba.jpg)

<!-- _footer: しんかわな, CC BY 3.0 <https://creativecommons.org/licenses/by/3.0>, ウィキメディア・コモンズ経由 -->

---

## 富士宮焼きそば

* 主に静岡県富士宮市周辺で食べられる焼きそば
* B-1グランプリ殿堂入り、NYで開催されたコナモングランプリで優勝

![h:300px](./images/fujinomiyashi-map.png) ![h:300px](https://lh3.googleusercontent.com/pw/AIL4fc_qzyqjAu3-1DV-HK-b02ln329d9Rsp45D1VYSlzc6Qpkk73NwvzCEXCLjjgXIGrCDq2pRNobz3dEnzgNjZHlcgEbmuMMV7cyksEf2O7dvMF2GHZ9zD)

<!-- _footer: 地元の人は、多分月に数回は食べてる -->

---

ところで、みなさん、

もう食べたくなりましたね？🤤

<!-- _footer: このあとはパーティ🎉ですし、お腹空きましたね🤤🍻 -->

---

# 富士宮焼きそばマップを作りましょう💪

---

# 今回のトークでできること

1. お店情報をデータにする: WEBスクレイピング
2. データを整形をする: CSVファイルにする
3. データを使ってみる: Googleマイマップで呼び出す

---

## 今回のトークでできること

![bg left:35% h:550px](./images/programing-flow.png)

1. お店情報をデータにする: WEBスクレイピング
2. データを整形をする: CSVファイルにする
3. データを使ってみる: Googleマイマップ

抽象的に言い直すと...

<p align="center">⬇️</p>

1. **どこから** データを取り出すか
2. **どんな** データを作るか
3. **どこへ** データを渡すか

---

## 1. どこからデータを取り出すか

![bg left:35% h:550px](./images/programing-flow.png)

* 🔍**WEBスクレイピングで収集する**
* [付録]🖼️画像識別で収集する

---

## ご当地グルメの情報はどこにあるか

* 地域情報を収集
* **その情報は機械可読ができるか？**
  * 大体が紙ベースが多い📃🐐 パンフレットとか
  * （画像識別の手段は使える）

観光情報を探ってみる

* 市役所、観光協会のWEBサイトで紹介されていたり
* ご当地グルメの公式サイト（よく〇〇学会とも言われる）

<!-- _footer: グルメ情報サイトを見たらそこで試合終了ですよ -->

---

今回は、富士宮焼きそば学会の公式サイトを例にしています。

<https://umya-yakisoba.com/shop/>

<!-- _footer: 富士宮焼きそば学会の公式サイトを見せます -->

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

この構造からBeautifulSoup4を使って必要な情報を取り出します。

![h:340px](./images/gakkai_1.png)　![h:340px](./images/gakkai_2.png)

---

![bg left:30% w:400px](./images/gakkai_1-1.png)

構造の中にあるタグから必要な情報を取得する

```python
import requests
from bs4 import BeautifulSoup

url = "https://umya-yakisoba.com/shop/"
shopinfo_list = []
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# ここではdiv.p-shopList > a にURLがある
# その中にお店情報がまとまっているので、aタグから取り出す
shopinfo_tags = soup.find(
  'div', class_='p-shopList'
  ).find_all("a")
```

---

![bg left:30% w:400px](./images/gakkai_1-2.png)

aタグの中にあるタグから必要な情報を取得する

```python
for shopinfo_tag in shopinfo_tags:
    shopdata = {}
    # divは上から店名、住所、電話番号、定休日。
    # ここではurlと店名だけまとめたリストを作る
    shopdata['specurl'] = shopinfo_tag.get('href')
    shopdata['店名'] = shopinfo_tag.find_all("div")[1].text
    
    shopinfo_list.append(shopdata)
```

---

お店の詳細URL, 店名が集まりました🎉

```python
>>> shopinfo_list
[{'specurl': 'https://umya-yakisoba.com/shop/3776/', '店名': 'お好焼 あき'},
 {'specurl': 'https://umya-yakisoba.com/shop/3777/', '店名': 'あさ家'},
 {'specurl': 'https://umya-yakisoba.com/shop/3774/', '店名': 'あるばとろす'},
 {'specurl': 'https://umya-yakisoba.com/shop/3616/', '店名': 'いっぷく亭'},
...
]
```

<!-- _footer: ※この例では店名に`\\u3000（全角スペースの意味）`が入ることがあり、半角スペースへ置き換え処理をした結果になります -->

---

収集した詳細URLのリストを使って、お店情報収集

![h:500px](./images/gakkai_2.png)

`dt`と`dd`タグは記述リスト、説明リストと呼ばれるHTMLタグ

---

![bg left:28% w:350px](./images/gakkai_2-1.png)

```python
for shopinfo in shopinfo_list:
    # URLから店舗情報を取得
    res = requests.get(shopinfo['specurl'])
    soup = BeautifulSoup(res.text, 'html.parser')

    # dl.p-shopDetails > dt/dd構造でdtが項目、
    # ddが値になっている。これを辞書形式にする
    shopspecs = {}
    for dt, dd in zip(
      soup.find('dl', class_='p-shopDetails').find_all('dt'),
      soup.find('dl', class_='p-shopDetails').find_all('dd')
    ):
        # 値に 改行や空白文字があるので取り除く
        shopspecs[dt.text] = dd.text

    # 店舗情報をマップ情報に追加
    shopinfo.update(shopspecs)
    # INFO:ここにランダム待機時間があるとよさそう
```

---

最終的にできるデータ🎉

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
  # 以下お店情報の辞書が続いて入る...
]
```

<!-- _footer: ※この例では各項目に`\\n（改行コード）`が入ることがあり、空白へ置き換え処理をした結果になります -->

---

## 上記コードの注意点

※: ⚠️WEBスクレイピングは注意が必要です
短時間で多数アクセスはやめましょう
ポリシーを守りましょう

※: サイト上に見えない文字があることがあります → 文字列置換をしましょう

※: この例ではサイトのページネーションに対応していません
ページネーションについては資料のコードで対応しています

---

## ⚠️WEBスクレイピングの注意点⚠️

**※スクレイピング対象のサイトへ短時間に多数のアクセスは
しないように注意しましょう**

* よくあるトラブル
  * ループ構造が深くてアクセス回数が膨れる
  * エラーの時にリトライし続ける
* **少し時間を置きながらアクセス**
  * ランダム時間置いてみる
  * 回数リミットをつけて待つ
* **サイトポリシーがあればそれに従う**
  * 利用規約を見る
  * （クローラー向けの）robot.txtを見る

<!-- https://umya-yakisoba.com/robots.txt -->
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

# 2~5秒の間でランダムに待つ
random_sleep(2, 5)
```

---

## 2. どんなデータを作るか

![bg left:35% h:550px](./images/programing-flow.png)

最後に利用するためのデータ（ファイル）を
作成します

* **💾情報を整理して表形式ファイルで書き出す**
* [付録]👣地理情報を集める

---

## 情報を整理

どのフォーマットで書き出すか？

よくある地理データ構造、ファイルフォーマット

* **CSV（カンマ区切り表形式、汎用性高）**
* GeoJSON（WEB APIで広く流通しているJSON形式の地理情報向け）
* KML（XML形式）

---

Python標準のCSVライブラリを使って書き出します

`csv.DictWriter`を使うと辞書のキーを使って列見出しを用意できる

```python
with open('mapdata.csv', 'w', newline='') as csvfile:
    # 注意:お店の詳細情報の各項目:辞書のキー が部分的に異なる。
    # 列名を統一するために全ての辞書のキーから全ての項目を集めたリストを生成
    csv_fieldnames = list(set().union(*shopinfo_list)

    writer = csv.DictWriter(csvfile, fieldnames=csv_fieldnames)
    writer.writeheader()
    for shopinfo in shopinfo_list:
        writer.writerow(shopinfo)
```
<!-- _footer: ※`変数:csv_fieldname`ではCSVの列名を統一するために、全ての辞書のキーを集めたリストを作成しています  -->
---

出力できたCSVファイル🎉

![h:300px](./images/csv1.png) ![h:300px](./images/csv2.png)

---

## 3. どこへデータを渡すか

![bg left:35% h:550px](./images/programing-flow.png)

旅行中に使うためのツールとして

* **巨人の肩に乗る:
🗺️Googleマイマップで使おう**
* [付録]🖨️ポータブルに扱う: 印刷をする
* [付録]🖥️専用のWEBアプリを作ろう

Googleマイマップとは

* オリジナルマップを作成できる
* スマホ版Googleマップでも表示可能

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

## そのほか選択肢

今回はGoogleマイマップを利用しましたが、推奨しているわけではなくて
データを作るといろんなサービスと連携できることをお伝えしました。

※: オリジナルのマップを作るサービスは他にも多数あります。一例を載せます
※: それぞれ特徴や無料有料とあるので、使いやすいものを探すと良いと思います

* OpenStreetMap uMap: <https://umap.openstreetmap.fr/ja/>
* proxi: <https://www.proxi.co/>
* [日本向け]国土地理院: <https://maps.gsi.go.jp/>
* etc...

---

# トークのまとめ

---

![bg left:35% h:550px](./images/programing-flow.png)

## 今回のトークでできること

1. お店情報をデータにする: WEBスクレイピング
2. データを整形をする: CSVファイルにする
3. データを使ってみる: Googleマイマップ

抽象的に言い直すと...

<p align="center">⬇️</p>

1. **どこから** データを取り出すか
2. **どんな** データを作るか
3. **どこへ** データを渡すか

---

**プログラミングでもっとも行われる行為**

* **どこから** データを取り出すか
* **どんな** データを作るか
* **どこへ** データを渡すか

プログラミングはデータの流れを意識しよう

---

* **どこから** データを取り出すか
  * データベースから取り出す
  * 現実の統計データを使う
  * センサーデータで現実環境を扱う
* **どんな** データを作るか
  * データを加工して新しいデータを作る
  * データを整形する
* **どこへ** データを渡すか
  * データの可視化をして分析
  * データを使って業務工程改善
  * データを使ってAIで予測

---

* **どこから** データを取り出すか
  * データベースから取り出す ➡️ データベース接続、API
  * 現実の統計データを使う ➡️ データセット、オープンデータ
  * センサーデータで現実環境を扱う ➡️ ハードウェア操作
* **どんな** データを作るか
  * データを加工して新しいデータを作る ➡️ 前処理、後処理
  * データを整形する ➡️ ファイル形式、データ構造
* **どこへ** データを渡すか
  * データの可視化をして分析 ➡️ グラフ、ダッシュボード
  * データを使って業務工程改善 ➡️ オートメーション、システム連携
  * データを使ってAIで予測 ➡️ 機械学習、ディープラーニング

<!-- _footer: データの流れを意識すると、作りたいプログラムの流れも理解しやすい -->

---

# 最後に伝えたいこと

PyCampやPythonの基礎を学んだ方の一歩先として。オススメです！

自分が使いたい、利用したい、ものやことがあればチャレンジしましょう！

できたら、とても楽しいし、感動します😆

---

**Happy Hacking!!**

**and, Have a nice trip!!**

---

# 付録

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
