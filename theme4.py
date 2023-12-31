import tkinter as tk

def create_stickman(canvas):
    stickman_parts = [
        canvas.create_oval(130, 50, 170, 90, fill="blue"),  # 頭部
        canvas.create_line(150, 90, 150, 150, fill="blue", width=2),  # 胴体
        canvas.create_line(150, 100, 180, 130, fill="blue", width=2),  # 右腕
        canvas.create_line(150, 100, 120, 130, fill="blue", width=2),  # 左腕
        canvas.create_line(150, 150, 180, 200, fill="blue", width=2),  # 右足
        canvas.create_line(150, 150, 120, 200, fill="blue", width=2)  # 左足
    ]
    return stickman_parts
    
# Tkインターフェイスを作成
root = tk.Tk()

# キャンバスを作成（ウィンドウ内に図形を描画する領域）
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

create_stickman(canvas)

# ウィンドウが閉じるまで実行
root.mainloop()