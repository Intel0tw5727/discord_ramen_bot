"""
read_ramen.py
ラーメン店舗の追加や削除などを行うモジュール
"""
import pandas as pd

def read_ramens():
    df = pd.read_csv("ramen_data.csv")
    return df

if __name__ == "__main__":
    print(read_ramens())
