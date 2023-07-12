import os
import json
import tkinter as tk

# JSONファイルを開く
def load_frame(frame_num):
    filename = f"kabeposter/kabeposter_{frame_num:012d}_keypoints.json"
    with open(filename) as f:
        data = json.load(f)
    return data

# 骨格の接続関係
skeleton = [
    (0, 1),  # 鼻 - 首
    (1, 2), (2, 3), (3, 4),  # 右腕
    (1, 5), (5, 6), (6, 7),  # 左腕
    (1, 8),  # 首 - 腰
    (8, 9), (9, 10), (10, 11),  # 右足
    (8, 12), (12, 13), (13, 14),  # 左足
]

# tkinterウィンドウの初期化
root = tk.Tk()
canvas = tk.Canvas(root, width=1000, height=1000)  # Adjust canvas size if necessary
canvas.pack()

def draw_frame(frame_num):
    canvas.delete("all")  # Clear the canvas

    data = load_frame(frame_num)

    # 各人の骨格を取得して描画
    for i, person_data in enumerate(data['people']):
        keypoints = person_data['pose_keypoints_2d']
        keypoints = [(keypoints[i], keypoints[i+1]) for i in range(0, len(keypoints), 3)]  # リストを座標のペアに変換

        # 人物ごとに色を変える
        color = "red" if i == 0 else "blue"

        # 骨格を描画
        for (i, j) in skeleton:
            canvas.create_line(keypoints[i][0], keypoints[i][1], keypoints[j][0], keypoints[j][1], fill=color)

    # If there are more frames, schedule the next one
    if frame_num < 99:  # assuming there are 100 frames numbered 0 to 99
        root.after(100, draw_frame, frame_num + 1)  # Change delay as needed

draw_frame(0)  # Start the animation

root.mainloop()