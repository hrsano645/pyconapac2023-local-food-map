# PyCon APAC 2023 「ご当地グルメマップを作ろう」

こちらは PyCon APAC 2023 の発表資料をまとめたリポジトリです。

スライドとサンプルコードを含みます。

## スライド

スライドは [slide/slide.pdf](slide/slide.pdf) にあります。

## サンプルコード

サンプルコードは [code](code) にあります。

### 環境作成

* Python 3.10以上（確認ずみ）

#### venv, requirements.txtを使う

```bash
> python -m venv venv

# windows
> venv\Scripts\activate
# macOS
> source venv/bin/activate

> pip install -r requirements.txt
```

#### オプション: ryeを使う

* Windows 11, macOSにて確認済み

ryeのインストール後、以下のコマンドを実行する。

```bash
> rye install
> rye sync
```
