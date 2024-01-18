from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import Menu
from tkinter import filedialog
from tkinter import scrolledtext



window = Tk()
window.title("Shmarin Danila Andreevich")
window.geometry('600x400')
tab_control = ttk.Notebook(window)
tab_1 = ttk.Frame(tab_control)
tab_2 = ttk.Frame(tab_control)
tab_3 = ttk.Frame(tab_control)
tab_control.add(tab_1, text = 'calc')
tab_control.add(tab_2, text = 'checkbx')
tab_control.add(tab_3, text = 'file')
tab_control.pack(expand=1, fill='both')




def res():
    a, b, c = chislo1.get(), dey.get(), chislo2.get()
    if b == "+":
        res1.configure(text = int(a) + int(c))
    elif b == "-":
        res1.configure(text = int(a) - int(c))
    elif b == "*":
        res1.configure(text = int(a) * int(c))
    elif b == "/":
        res1.configure(text = int(a) / int(c))

chislo1 = Entry(tab_1, width=5)
chislo1.grid(column=0, row=0)
chislo2 = Entry(tab_1, width=5)
chislo2.grid(column=2, row=0)

dey = Combobox(tab_1, width=5)
dey['values'] = ('+', '-', '*', '/')
dey.grid(column=1, row=0)

bt = Button(tab_1, text='=', width=5, command=res)
bt.grid(column=4, row=0)

res1 = Label(tab_1)
res1.grid(column=5, row=0)







def checkbox():
    a,b,c = chk1_value.get(),chk2_value.get(),chk3_value.get()
    if a == b == c == "":
        mb.showinfo("Ahtung", "Viberi variant")
        return
    mb.showinfo("Confirm", f"Vi vibrali {a} {b} {c}")

chk_btn = Button(tab_2, text="Confirm", command=checkbox)
chk_btn.grid(column=0, row=5)

chk1_value = StringVar()
chk2_value = StringVar()
chk3_value = StringVar()

chk_1 = Checkbutton(tab_2, text='1 variant', variable=chk1_value, onvalue="1 variant", offvalue="")
chk_1.grid(column=0, row=0)
chk_2 = Checkbutton(tab_2, text='2 variant', variable=chk2_value, onvalue="2 variant", offvalue="")
chk_2.grid(column=0, row=1)
chk_3 = Checkbutton(tab_2, text='3 variant', variable=chk3_value, onvalue="3 variant", offvalue="")
chk_3.grid(column=0, row=2)



def download():
    file_name = filedialog.askopenfilename(filetypes=(("All", "*"), ("Text", "*.txt")))
    with open(file_name, "r") as f:
        txt.insert(INSERT, f.read())

txt = scrolledtext.ScrolledText(tab_3)
menu3 = Menu(window)
window.config(menu = menu3)
file_menu=Menu(menu3, tearoff=0)
file_menu.add_command(label="Download", command=download)
menu3.add_cascade(label='file', menu=file_menu)

txt.pack(expand=1, fill="both")





window.mainloop()
