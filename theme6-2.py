import json
import tkinter as tk

# JSONファイルを開く
with open('kabeposter/kabeposter_000000000000_keypoints.json') as f:
    data = json.load(f)

# tkinterウィンドウの初期化
root = tk.Tk()
canvas = tk.Canvas(root, width=1000, height=1000)  # Adjust canvas size if necessary
canvas.pack()

# 肩の座標を抽出
person1_data = data['people'][0]['pose_keypoints_2d']
person2_data = data['people'][1]['pose_keypoints_2d']

# OpenPoseの出力は（x, y, confidence）の順になっているので、肩の座標のインデックスを計算
# 右肩=2, 左肩=5
rshoulder_index = 2 * 3  # 2(右肩のインデックス) * 3(各関節のデータ数)
lshoulder_index = 5 * 3  # 5(左肩のインデックス) * 3(各関節のデータ数)

# 肩のラインを描画
canvas.create_line(person1_data[rshoulder_index], person1_data[rshoulder_index + 1],
                   person1_data[lshoulder_index], person1_data[lshoulder_index + 1], fill='red')

canvas.create_line(person2_data[rshoulder_index], person2_data[rshoulder_index + 1],
                   person2_data[lshoulder_index], person2_data[lshoulder_index + 1], fill='blue')

root.mainloop()