# search_lang_demand_amount
指定した言語がどのくらい需要があるかを検索するツール

# 使い方
## 単品使用

python3.6 main.py 言語リスト

言語リストはJson形式のリスト表記。例:
python3.6 main.py '["Python", "C言語", "Ruby"]'

## cgi等で使用

`from search_lang_demand_amount import slda_main`後、`slda_main(args)`を実行する。
resultはdict形式の以下のような形式となる。

```
{
  "#google":"google検索の値",
  "google":{
    "result_denominator":分母値,
    "result_numerator":分子値
   },
  "#levatech":"levatech求人検索の値",
  "levatech":{
    "result_denominator":分母値,
    "result_numerator":分子値
   },
  "#qiita":"qiita検索の値",
  "qiita":{
    "result_denominator":分母値,
    "result_numerator":分子値
   }
}
```

# 環境
必須:
```
pip3 install bs4
```

- Qiita API使用のため、アクセストークンの取得が必要です。
トークン発行URL
https://qiita.com/settings/tokens/new

- 動作確認環境

python 3.6
Ubuntu 18.04, Windows 10(windwosの場合はJson文字列内"に\を付ける必要あり)
