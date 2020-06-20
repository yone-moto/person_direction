pose angular
====

openposeの出力から角度を算出するプログラム

## Description
openposeから関節点を取得して、その関節点の位置を入力として

勾配ブースティングの一種である、LightGBMを使って解析するプログラム。

分類問題としており、0,30,60,90,120,150,180,-150,-120,-90,-60,-30の出力が得られる。

## 構成

-raw_data(トレッドミル（ルームランナー）で取得したデータ（jsonファイル）trainとtest用)

-input_data (row_dataを加工したcsvファイルを保存するフォルダ)

-model (学習したmodelを保存するフォルダ)

-output (学習したmodelでtestの結果を保存するフォルダ)

## Usage

1. raw_dataをjsonからdataframe(csv)形式にして成形する

   make_dataframe.ipynbを実行

   dataframe(csv)がinput直下に作られる。
   
2. 欠損値を埋める

   df_ffill.ipynbを実行

   新しいdataframe(csv)がinput直下に作られる。

3. モデルの学習を行う
"""
   python lightgbm_model.py
"""
4. テストデータで評価する
"""
   python lightgbm_test.py
"""
