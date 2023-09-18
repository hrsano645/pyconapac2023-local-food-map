---
marp: true
---

# ご当地グルメマップを作ろう  

# Lets create Local Food Map

## PyCon APAC 2023 10/25

Hiroshi Sano

![width:200px](./images/pyconapac2023_logo.png)

---

## Agenda

* トークのモチベーション
* 情報を集めよう: どの情報を使うか
* マップデータを作ろう: 情報収集をアウトプット
* 利用先を考えよう: サービスと連携しよう

---

## 今回の資料

付録含めてすでに公開されています。

* github: Starくれー！
* このslide

あとでトライしたい方は参考にしてね

---

## Self Infroduction

Hiroshi Sano(佐野浩士) [@hrs_sano645](https://twitter.com/hrs_sano645)

* 🏢: [株式会社佐野設計事務所](https://sano-design.info)  Founder
* 🐍: PyCon mini Shizuoka Stuff
* shizuoka.py / Unagi.py / PythonSurugaCivicTech, [Startup Weekend Oganizatior](https://swfuji.doorkeeper.jp)
* Hobby: DIY⚒️, IoT, Camp🏕️

<!-- ここに画像をいくつか並べる PyCon shizu , DIY, CAMPとか 200x200で-->

![w:200px](./images/sns-logo.jpg)![w:300px](./images/shizuokaLogo.png) ![w:200px](https://lh3.googleusercontent.com/pw/AIL4fc9DDT9ootdGiDNZiGUybbHE5WRnm68hFp6XknmZc2lVttIBKJ180GVq0NE2qtcGRbx8OBVAak3E4qHa7H5iXw8gtQqkY4l6tWrFkIHUA96q1jcqE2_f) ![w:200px](https://lh3.googleusercontent.com/pw/AIL4fc_3zxLYLoa5SSL_apqpJ3WCY9BRMfXRL4jUYaYouX3MvqiMU5eSCi8be6eQIvboRzgNZ3ZvdZAIET40tJD7I4y8dSHF6UByo-u8jXhLFFGv5rAw_kZU)

---

## 弊社紹介

< 一枚絵の画像で、やっていることを紹介する >

---

## トークのモチベーション

* ご当地のグルメの**情報収集してマップを作り**ましょう！食べに行きましょう！
* PyCampを終えた人向け: **Pythonでデータを集めて作り利用するプロセス**
  を学べます

---

## PyCampとは

* 日本全国で開催されているPythonの学習プログラム
* Pythonの基礎から最後にプログラムを作るところまでを半日で行う
  * 地元静岡県だと3回開催

<!-- ここに3枚の静岡開催の写真を載せる -->
![h:250px](https://lh3.googleusercontent.com/pw/AIL4fc-QihRkRpnkffJ9b1pmbmM6J4Jc4hkDXCleYASV-peLtXU9USqbL41kQjl85yDJAjUrSDFe0yDxO-ygY-U0TlYC1vhW7z5dmeOFBok8Z1wA9mXsbrIR) ![h:250px](https://lh3.googleusercontent.com/pw/AIL4fc9_J_x8gcqjZ828PuiB3sVh7FjhZW8ZTWXSzBOZSZxTFh9dnbBIvTU2KsnQGH7iZacfkPJix4lsezINDWNERljbRgfUPFjAKFkDFgtuXI1OzJegQRhy) ![h:250px](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjS_cCQlBadAUmQnxucUD5NjwxcSqAJzILkL7ng1PEgrKqPh8mvT8KkHd1XueX40o_DydsBO6iNB8K3HWdOnXb0csUkMQ3th9uBbFJ9DkB4qEQgY6X43vM9s0ieoYgsitSTU-6VdXvxaGvfMyVH1ZRk5WALgXjR7bHXY4SFmOZo0x5_hhSEHpfe7h68/s5472/IMG_5991.jpg)

このトークはその続きからトライできるコンテンツを目指して作りました

---

![bg left:40%](./images/programing-flow.png)

PyCampの次にトライできるものとして

* データを読む/取り込む
* データを加工/出力する
* データを使う/活用する

3つの流れで、ご当地グルメマップを作ります

<!-- （この3つをフローチャートで置いた画像を横に並べる -> flow.png） -->

---

## ご当地グルメ

* 旅行がしやすくなった昨今
* 観光地でご飯食べようにも色々悩む
  * 情報サイトは有名なものだらけ。美味しいところは他にもある
* 公開されている情報をもとにマップを作って旅行計画するのはいかがでしょう？

---

## 今回のお題

---

## 富士宮焼きそば

![h:500px](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Fujinomiya-yakisoba.jpg/800px-Fujinomiya-yakisoba.jpg)

<!-- _footer: しんかわな, CC BY 3.0 <https://creativecommons.org/licenses/by/3.0>, ウィキメディア・コモンズ経由 -->

---

* 主に静岡の富士宮市周辺で食べられる焼きそば
* B級グルメグランプリは殿堂入り

---

家庭料理として、家でも作ります

![h:400px](https://lh3.googleusercontent.com/pw/AIL4fc_qzyqjAu3-1DV-HK-b02ln329d9Rsp45D1VYSlzc6Qpkk73NwvzCEXCLjjgXIGrCDq2pRNobz3dEnzgNjZHlcgEbmuMMV7cyksEf2O7dvMF2GHZ9zD) ![w:400px](https://lh3.googleusercontent.com/pw/AIL4fc_qwaQCAlWagvvYmD6H9CvvnwXuWQRRi5REJr1_IF9nFP31GGuv3kJz6F7JKdIrYqs3mNANLi2IdXeUTWLDVHIuXnjbrFITbMtd5HxjEbYCVejEjsYQ)

<!-- 麺が中太蒸し麺。富士宮市で生産されている -->

---

もう食べたいでしょ？🤤

---

富士宮焼きそばマップを作りましょう！

---

## 今回のトークでの成果

* お店情報をWEBスクレイピング
* 表形式に整形 -> CSVファイル
* Googleマイマップで呼び出す

---

## ご当地グルメの情報はどこにあるか

（img:flow.png）

* 地域の情報を収集
* そこの情報は機械可読性があるか

---

観光情報

* 市役所
* 観光協会
* ご当地グルメの公式サイト（よく〇〇学会とも言われる）

---

富士宮焼きそば学会の公式サイト

---

## データを読む/取得する

（img:flow.png）

* Webスクレイピングで収集する
* 画像識別で加工を試みる

機械可読性はどちらも微妙だが、WEBスクレイピングはやりやすい

---

機械可読性はどちらも微妙だが、WEBスクレイピングはやりやすい

※ただし多量のアクセスはしないように注意

---

サイトの構造

---

（構造で取りたい情報をマッピング）

---

店名 +

requests + Beautiful Soup4

```python
# <コード>
```

---

取得結果

```python
# <コード>
```

---

少し余分な情報を外します

```python
# <コード>
```

---

ページネーションに対応する

URLをもとに、アクセスする→エラーの場合は終了

```python
# <コード>
```

---

収集した詳細URLのリストを使って、お店情報収集

```python
# <コード>
```

---

最終的にできるデータ

<データの様子>

---

## データを加工/出力する

（img:flow.png）

マップのもとになるデータを作成します

* 情報を整理して書き出す
* [appendex]地理情報を集める

---

情報を整理

どのフォーマットで書き出すか

---

よくある地理データ構造

* CSV（区切り表形式）
* GeoJSON（WEB APIで広く流通しているJSON形式の地理情報向け）
* KML（XML形式）

（どのような使い方にもよります。他にもあったら教えてください）

---

CSVライブラリを使って書き出せます

```python
# <コード>
```

---

ちょっと一工夫: それぞれ入っているデータ項目が違う

-> 全部対応した項目を一度作り、列見出し（ヘッダ）にする

```python
# <コード>
```

---

## データを使う/活用する

旅行中に使うためのツールとして

* 巨人に乗る: Googleマイマップを使おう
* [appendex]ポータブルに扱う: 印刷をする
* [appendex]専用のWEBアプリを作ろう

---

Googleマイマップで読み込もう

（説明しながら、図式を載せて使い方を見せていく）

---

やっぱりスマホで使えると便利

---

## まとめ

---

![bg left:40%](./images/programing-flow.png)

## 今回のトークでの成果

* お店情報をWEBスクレイピング
* 表形式に整形 -> CSVファイル
* Googleマイマップで呼び出す

---

今日学んだことを応用すると

* WEBスクレイピングでデータ収集 -> 世の中のWEBサイトの収集
（※一応扱いには気をつけましょう
* WEB APIの扱いができると収集はもっと楽
* データの書き出し: CSV以外にもjson, xlsx（openpyex, etc...）
* 画像識別で収集
* 他のサービスへの連携:

（今回の知識をベースに何ができるか、各工程で２つぐらいは出しておく）

---

どのエンジニアが一番やること

* データを呼ぶ
* データを書き出す

---

* どこからデータを呼ぶか
  * データベースから使う
  * データ分析で現実の統計データを使う
  * センサーデータで現実環境を使う
* データを書き出すと
  * ユーザー情報をもとにレコメンデーション
  * データ分析でサービス改善
  * センサーデータから製造工程改善

これができると、仕事もですが、人生まで改善できると思う。

---

PyCampやプログラミングを学んだ方の一歩先として！

自分が使いたい、利用したいものやことでトライする。

できたらとても楽しいし感動する。おすすめ！

---

### Let's try

### ハッピーハッキング

### And, 楽しい旅行を

---

## appendex

今回扱わなかった他の方法については、またどこかで解説できたら

* 画像識別で収集する
* 緯度経度を収集
* 印刷物を作る -> HTML+テンプレートエンジンで印刷しやすいデータを生成
* fletでWEBアプリを作る
