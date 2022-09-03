import pyshorteners
from tkinter import *
from tkinter import ttk


def url_shortener():
    s = pyshorteners.Shortener()
    link_before = long_link.get()
    short_link.delete(0, END)
    short_link.insert(0, s.tinyurl.short(link_before))


root = Tk()
root.title("Сокращатель ссылок")
root.geometry("400x200")
root.resizable(width=False, height=False)

long_link_label = Label(root, text="Вставьте ссылку")
long_link_label.place(x=10, y=10)

long_link = ttk.Entry(root, width=40, font="Arial 12")
long_link.place(x=10, y=30)

btn = ttk.Button(root, text="Сократить", command=url_shortener)
btn.place(relx=0.5, y=70, anchor=CENTER)

short_link_label = Label(root, text="Результат")
short_link_label.place(x=10, y=100)

short_link = ttk.Entry(root, width=40, font="Arial 12")
short_link.place(x=10, y=120)


root.mainloop()