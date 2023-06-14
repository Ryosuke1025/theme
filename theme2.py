import json

# JSON ファイルを開き、データを読み込む
with open('catalog.json', 'r') as file:
    data = json.load(file)

# jacket のデータのみを取得
jacket_data = [item for item in data if item['name'] == 'jacket']

# jacket の個数を求める
num_jackets = len(jacket_data)

# jacket の最高価格を求める
max_price = max(item['price'] for item in jacket_data)

# jacket の最低価格を求める
min_price = min(item['price'] for item in jacket_data)

print(f"Number of jackets: {num_jackets}")
print(f"Max price: {max_price}")
print(f"Min price: {min_price}")