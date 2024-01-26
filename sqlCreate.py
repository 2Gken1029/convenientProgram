#! /usr/bin/env python3
import random
import secrets
from faker import Faker
import pykakasi

kks = pykakasi.kakasi()

# 指定範囲の数値をランダムに取得 random.randint(0, 3)
# 名前の生成 Faker().name()
# emailアドレスの生成（重複を避けるために0から9999までのランダムな数字を生成） f"email{secrets.randbelow(10000)}@example.com"  #
# 10桁のランダムな数字を生成 "".join(str(random.randint(0, 9)) for _ in range(10))
# 指定要素の中からランダムに取得 random.choice(["要素1", "要素2", "要素3"])
# 適当な桁数の文字列数値を生成（例は3桁） f"{random.randint(100, 999)}"
# ランダムなバイト数の文字列を生成（例は6バイト） f"{secrets.token_hex(6)}"


# ダミーデータを生成するための関数例
def generate_dummy_admin_data(i):
    id = i
    name = Faker().name()
    email = f"email{secrets.randbelow(10000)}@example.com"  # 0から9999までのランダムな数字を生成
    email_verified_at = None
    password = secrets.token_hex(8)  # ランダムな8バイトの文字列を生成
    role = random.randint(0, 2)
    remember_token = "null"

    return (id, name, email, email_verified_at, password, remember_token)


# 40個のダミーデータを生成
dummy_data = [generate_dummy_admin_data(i) for i in range(40)]
# SQLのINSERT文を作成
sql_insert_template = "INSERT INTO admin_users (id, name, email, email_verified_at, password, remember_token) VALUES "
sql_values = ",\n".join(str(data) for data in dummy_data)
sql_insert_statement = sql_insert_template + sql_values + ";"
# SQLのINSERT文を表示
print(sql_insert_statement)
