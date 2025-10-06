import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.geometry("600x400")

input_name = tk.Entry(win)
input_phone = tk.Entry(win)
label_name = tk.Label(win, text="Nombre: ")
label_phone = tk.Label(win, text="Telefono: ")
tree_agenda = ttk.Treeview(win, columns=("id","name","phone"), show="headings")

agenda = []

def add(): 
    name = input_name.get()
    phone = input_phone.get()
    id = len(agenda)+1

    agenda.append([id, name, phone])
    update()
    input_name.delete(0,tk.END)
    input_phone.delete(0,tk.END)

def update():
    for elem in tree_agenda.get_children(): 
        tree_agenda.delete(elem)
    for contact in agenda:
        tree_agenda.insert("","end",values=(contact[0],contact[1],contact[2]))


btn_add = tk.Button(win, text="AÑADIR", command=add)

label_name.pack()
input_name.pack(pady=(0,20))
label_phone.pack()
input_phone.pack(pady=(0,20))
btn_add.pack()
tree_agenda.pack(pady=20)


tree_agenda.heading("id",text="ID")
tree_agenda.heading("name",text="NAME")
tree_agenda.heading("phone",text="PHONE")

tree_agenda.column("id", anchor="center")
tree_agenda.column("name", anchor="center")
tree_agenda.column("phone", anchor="center")

win.mainloop()