# メモ

今回のトークで言いたいことをまず考える

* ここでは富士宮焼きそばのまっぷを作るためのデータを生成する
* データ生成ノウハウ的なことを伝えることにしてみる。
* データの取得と出力の間の前処理が結構大変なのよね。ここがあることがわかるとデータを作るという作業に馴染めると思う。

---

深く考えてみる。

今回のテーマは、旅行しやすいし、行き先やもちろん地元もOK、地域のグルメ情報を自分たちで作ってみるをやってみる。

地元のB級グルメを食べ歩いてみたい -> お店が多数ある。 マップデータにして、データを使ってどのお店に行こうかを考えてみる。

たとえば、例を挙げてみる

* 近くに来たらすぐに探せるようにする。マップと現在地をみるとか
  * Googleマップにデータを持っていく
* 食べた場所を記録するときに使う
  * スプレッドシート + ノーコードツールで手軽にアプリ化してみる
* 歩ける場所を絞って、地域ごとにグルーピングをして食べ歩いてみるとか
  * データ分析的に使う:

もう1つ、

PyCampの一歩先でPythonを使ってみようというテーマでやってみようかと思う。

今回のコードはPyCampで出てきた話がほとんど。（type hintはあるけどそこが重要ではない）

一歩先は
プログラミングで何かを解決する -> データを作って利用する ところまでできると、いろんな方法に使うことができる。

プログラミングは多くはデータを作って使うが基本になると思う。身近な課題はほとんどこの方法で解決できる。

これを裏の目的にして、出発点を一合わせする。

---

中身考えていく。

* 15分なので、マップデータを作る、ひとまず表示する。使うときの方法論を挙げて終わり
* 初学者にもできるように、テーマを絞っていく。スクレイピング、マップデータとして使いたい時の方法論
  * pycamp向けにrequests, selenium + bs4
    * 画像情報はappendexとして クラウドのサービスで（Google Cloud Vision API） → 富士市つけナポリタン、ゆるキャン△聖地のマップを例にする
  * Googleマップとumap（OSM）を使う → 無料でどちらも使える。餅は餅屋に任せる
  * 印刷（HTML生成してPDF化印刷）とかFletはappendexにしておく
  * 点群とかGeoPandasとかは一切登場しない

ご当地ぐるめの地図作成。データをメインに扱って、書き出しなどはいろんなサービスを頼る戦略にする

fletでアプリ化して、公開できるようにしてもいいところで、用意する

* fletで地図を扱うときに画像埋め込みにするかなと思ったけど、Plotlyのチャートが使えるらしいから、mapもできるかも。試してみる
  * [PlotlyChart | Flet](https://flet.dev/docs/controls/plotlychart#box-chart "‌")
* そのほか調べていたもの
  * [fultter open street map - Google 検索](https://www.google.com/search?q=fultter+open+street+map&sourceid=chrome&ie=UTF-8 "‌")
    [flet plotly - Google 検索](https://www.google.com/search?q=flet+plotly&sxsrf=APwXEddFqDpLbPJzzlZfzSh14RGXy_QXVQ%3A1686834534776&ei=Zg2LZJSDL8vWhwOMoZHgAQ&ved=0ahUKEwiUzvWprMX_AhVL62EKHYxQBBwQ4dUDCA8&uact=5&oq=flet+plotly&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQgAQyCAgAEAUQHhAKOgcIIxCwAxAnOgoIABBHENYEELADOgcIABCKBRBDOgkIABATEIAEEAo6CAgAEB4QExAKOgkIABAeEPEEEBM6BggAEAgQHkoECEEYAFCUBliQDWCMEWgCcAF4AIABZogBzQSSAQM1LjGYAQCgAQHAAQHIAQo&sclient=gws-wiz-serp "‌")
    [PythonでWebアプリ作れるやつのまとめ(8選)](https://zenn.dev/neka_nat/articles/f2f5b6ebeb049a "‌")
    [flet | Flutter Package](https://pub.dev/packages/flet "‌")
    [Matplotlib と Plotly チャート | フレット](https://flet.dev/blog/matplotlib-and-plotly-charts/ "‌")
    [examples/python/controls/charts-plotly/plotly-barchart.py at main · flet-dev/examples · GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/charts-plotly/plotly-barchart.py "‌")
    [Lines on mapbox in Python](https://plotly.com/python/lines-on-mapbox/ "‌")
    [Exploring Flet | Building Flutter Apps in Python | by Mustafa Tahir | Medium](https://medium.com/@mustafatahirhussein/exploring-flet-building-flutter-apps-in-python-1b680db5add2 "‌")
    [Flutter for Python Developers | Flet | Cross platform Development in Python - YouTube](https://www.youtube.com/watch?v=ZSdCA8-sMj4 "‌")
    [flutter\_osm\_plugin | Flutter Package](https://pub.dev/packages/flutter_osm_plugin "‌")

---

この先は最後に付け足せたら付け足す。

* 地域のグルメ情報はデータで落ちてないことが多い。
* それって他の情報も同じ。ゴミとか、地域の回覧板とか
* データを作れる人たちを増やしていくのが、今後の社会課題になると思う。
* でもそんなに肩張るような話ではない。そうやって誰でも作れる、扱えるようになることで、社会の情報の扱い方がまた変わっていくはずが仮説としてあって、それの取り組み
をしてみてる。
