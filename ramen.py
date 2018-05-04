"""
read_ramen.py
ラーメン店舗の追加や削除などを行うモジュール
"""
import pandas as pd

def read_ramens(df):
    return df

def add_ramen(sentence):
    return None

def list_ramen(df):
    return df.name.tolist()    

if __name__ == "__main__":
    df = pd.read_csv("ramen_data.csv")
    print(read_ramens())
