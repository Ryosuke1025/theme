def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
total = 0  # 合計値を保存する変数

# ファイルを開く
with open('data.txt', 'r') as file:
    for line in file:  # ファイルの各行に対して
        stripped_line = line.strip()  # 行の両端の空白を削除
        if is_integer(stripped_line):
            total += int(stripped_line)

print(total)  # 合計値を表示