"""
read_ramen.py
ラーメン店舗の追加や削除などを行うモジュール
"""
import pandas as pd

def read_ramens(df):
    return df

def add_ramen(sentence):
    return None

def list_ramens(df):
    return df.name.tolist()    

def set_ramen(sentences):
    with open("ramens_list.csv", "a") as f:
        f.write("{},{}".format(sentences[0], sentences[1]))
    print("Writed")
