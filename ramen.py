"""
read_ramen.py
ラーメン店舗の追加や削除などを行うモジュール
"""

def read_ramen():
    ramens = []
    with open("ramen_list.txt", "r") as f:
        for r in f.readlines():
            ramens.append(r.replace("\n", ""))
    return ramens

if __name__ == "__main__":
    print(read_ramen())
