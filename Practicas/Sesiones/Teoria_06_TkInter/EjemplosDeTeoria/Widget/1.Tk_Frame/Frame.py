import tkinter as tk

root = tk.Tk()
root.geometry("720x350")

frame = tk.Frame(root)
frame.config(width="350", height="200")
frame.config(borderwidth='10', relief='groove')
frame.config(bg="red")

frame.pack(side="right")  # 'left', 'right', 'top', 'bottom'

root.mainloop()
