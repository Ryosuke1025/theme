import tkinter as tk

# Tkインターフェイスを作成
root = tk.Tk()

# キャンバスを作成（ウィンドウ内に図形を描画する領域）
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# 頭部を描画 (外接する矩形の対角の座標)
canvas.create_oval(130, 50, 170, 90, fill="blue")

# 胴体を描画 (始点と終点の座標)
canvas.create_line(150, 90, 150, 150, fill="blue", width=2)

# 右腕を描画 (始点と終点の座標)
canvas.create_line(150, 100, 180, 130, fill="blue", width=2)

# 左腕を描画 (始点と終点の座標)
canvas.create_line(150, 100, 120, 130, fill="blue", width=2)

# 右足を描画 (始点と終点の座標)
canvas.create_line(150, 150, 180, 200, fill="blue", width=2)

# 左足を描画 (始点と終点の座標)
canvas.create_line(150, 150, 120, 200, fill="blue", width=2)

# ウィンドウが閉じるまで実行
root.mainloop()