import os

# sampleフォルダのパスを指定
directory = 'sample'

# 合計を0で初期化
total = 0

# ディレクトリ内の全ファイルをループで処理
for file_name in os.listdir(directory):
    print(file_name)
    # ファイル名がkitamura_******_kug.txtの形式に一致するかチェック
    if file_name.startswith("kitamura_") and file_name.endswith("_kgu.txt"):
        # ファイル名から数字部分を抽出
        number_part = file_name[len("kitamura_"):-len("_kgu.txt")]
        print(number_part)
        # 数字部分が奇数かどうかをチェック
        if int(number_part) % 2 == 1:
            # ファイルを開いて中の整数を合計に加算
            with open(os.path.join(directory, file_name), 'r') as file:
                total += int(file.read().strip())

# 最終的な合計を表示
print(f"奇数のファイルに書かれた数字の合計: {total}")