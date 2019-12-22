import tkinter as tk


def print_display():
    print(buff.get())
    buff.set("")


root = tk.Tk()

# 共通のフォント指定
root.option_add("*Font", "Consolas 14")

# タイトル
root.title("テスト")

# 画面大きさと位置
root.geometry("300x150+500+200")

# 変数
buff = tk.StringVar()

# get()で値の取得、set()で値の設定
buff.set("")

# ウィジェット
label1 = tk.Label(root, text="何か一言")
entry1 = tk.Entry(root, textvariable=buff)
button1 = tk.Button(root, text="クリック", command=print_display)

# 配置
label1.grid(row=0, column=1, pady=10)
entry1.grid(row=0, column=2)
button1.grid(row=1, column=2, sticky="EW")


root.mainloop()
