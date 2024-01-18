import tkinter as tk
import json
import requests

window = tk.Tk()
window.title("Shmarin Danila Andreevich")
window.geometry("600x400")
def info():
    username = vvod.get()
    url = f"https://api.github.com/users/{username}"
    udata = requests.get(url).json()
    information = ("company", "created_at", "email", "id", "name", "url")
    dt = {}
    for i in information:
        dt[i] = udata.get(i)
    with open("data_file", 'w') as file1:
        file1.write(json.dumps(dt, indent=2))
ll = tk.Label(window, text="Username: ")
ll.grid(column=0, row=0)

vvod = tk.Entry(window)
vvod.grid(column=1, row=0)

bt = tk.Button(window, text="Confirm", width=12, command=info)
bt.grid(column=2, row=0)

window.mainloop()
