import tkinter as tk
import subprocess


def ydl():
    url = buff.get()
    if url.startswith("http"):
        # youtube-dl が入っている前提
        # Windowの例
        command = f"start youtube-dl {url}"
        # 子プロセスの終了を待たない
        subprocess.Popen(command.split(), shell=True)

    buff.set("")


root = tk.Tk()

# 共通のフォント指定
root.option_add("*Font", "Consolas 12")

# タイトル
root.title("テスト")

# 画面大きさと位置
root.geometry("500x150+500+200")

# 変数
buff = tk.StringVar()

# get()で値の取得、set()で値の設定
buff.set("")

# ウィジェット
label1 = tk.Label(root, text="url")
entry1 = tk.Entry(root, textvariable=buff, width=50)
button1 = tk.Button(root, text="クリック", command=ydl)

# 配置
label1.grid(row=0, column=1, pady=10)
entry1.grid(row=0, column=2)
button1.grid(row=1, column=2, sticky="EW")


root.mainloop()
