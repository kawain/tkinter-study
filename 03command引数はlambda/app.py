import tkinter as tk


def print_display(s):
    print(s)


root = tk.Tk()

root.title("テスト")
root.geometry("300x150+500+200")

# ウィジェット
button1 = tk.Button(root, text="クリック", command=lambda: print_display("こんにちは"))

# 配置
button1.grid()


root.mainloop()
