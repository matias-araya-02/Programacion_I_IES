import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Variables globales
agenda = []
selected_contact_id = None

# Función para limpiar campos
def clear_inputs():
    input_name.delete(0, tk.END)
    input_phone.delete(0, tk.END)

# Función para actualizar la visualización
def update_display():
    # Limpiar el treeview
    for elem in tree_agenda.get_children(): 
        tree_agenda.delete(elem)
    
    # Mostrar contactos según el filtro
    for contact in agenda:
        if show_deleted.get() or contact[3]:  # Mostrar todos o solo activos
            status = "Activo" if contact[3] else "Eliminado"
            tree_agenda.insert("", "end", values=(contact[0], contact[1], contact[2], status))

# Función para añadir contacto
def add_contact(): 
    name = input_name.get().strip()
    phone = input_phone.get().strip()
    
    if not name or not phone:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos")
        return
    
    id = len([c for c in agenda if c[3]]) + 1  # Solo cuenta contactos activos
    agenda.append([id, name, phone, True])  # True = activo
    update_display()
    clear_inputs()
    messagebox.showinfo("Éxito", "Contacto añadido correctamente")

# Función para cancelar edición
def cancel_edit():
    global selected_contact_id
    selected_contact_id = None
    btn_add.config(text="AÑADIR", command=add_contact, bg="green")
    clear_inputs()

# Función para actualizar contacto
def update_contact():
    global selected_contact_id
    if selected_contact_id is None:
        return
    
    name = input_name.get().strip()
    phone = input_phone.get().strip()
    
    if not name or not phone:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos")
        return
    
    # Buscar y actualizar el contacto
    for contact in agenda:
        if contact[0] == selected_contact_id:
            contact[1] = name
            contact[2] = phone
            break
    
    update_display()
    clear_inputs()
    cancel_edit()
    messagebox.showinfo("Éxito", "Contacto actualizado correctamente")

# Función para editar contacto
def edit_contact():
    selected = tree_agenda.selection()
    if not selected:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un contacto para editar")
        return
    
    item = tree_agenda.item(selected[0])
    contact_id = int(item['values'][0])
    
    # Buscar el contacto en la agenda
    contact = next((c for c in agenda if c[0] == contact_id), None)
    if not contact:
        messagebox.showerror("Error", "Contacto no encontrado")
        return
    
    if not contact[3]:  # Si está eliminado
        messagebox.showwarning("Advertencia", "No se puede editar un contacto eliminado")
        return
    
    # Llenar los campos con los datos actuales
    input_name.delete(0, tk.END)
    input_phone.delete(0, tk.END)
    input_name.insert(0, contact[1])
    input_phone.insert(0, contact[2])
    
    global selected_contact_id
    selected_contact_id = contact_id
    
    # Cambiar el botón añadir por actualizar
    btn_add.config(text="ACTUALIZAR", command=update_contact, bg="purple")

# Función para eliminar contacto (eliminación lógica)
def delete_contact():
    selected = tree_agenda.selection()
    if not selected:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un contacto para eliminar")
        return
    
    item = tree_agenda.item(selected[0])
    contact_id = int(item['values'][0])
    
    # Confirmar eliminación
    if messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este contacto?"):
        # Buscar y marcar como eliminado
        for contact in agenda:
            if contact[0] == contact_id:
                contact[3] = False  # False = eliminado
                break
        
        update_display()
        messagebox.showinfo("Éxito", "Contacto eliminado correctamente")

# Función para restaurar contacto
def restore_contact():
    selected = tree_agenda.selection()
    if not selected:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un contacto para restaurar")
        return
    
    item = tree_agenda.item(selected[0])
    contact_id = int(item['values'][0])
    
    # Buscar y restaurar el contacto
    for contact in agenda:
        if contact[0] == contact_id and not contact[3]:
            contact[3] = True  # True = activo
            break
    
    update_display()
    messagebox.showinfo("Éxito", "Contacto restaurado correctamente")

# Evento para doble clic en el treeview
def on_double_click(event):
    edit_contact()

win = tk.Tk()
win.geometry("800x600")
win.title("Agenda de Contactos - CRUD")

# Crear la variable después de la ventana principal
show_deleted = tk.BooleanVar()

# Widgets de entrada
frame_form = tk.Frame(win)
frame_form.pack(pady=10)

label_name = tk.Label(frame_form, text="Nombre: ")
label_name.grid(row=0, column=0, sticky="w", padx=(0,10))
input_name = tk.Entry(frame_form, width=30)
input_name.grid(row=0, column=1, padx=(0,20))

label_phone = tk.Label(frame_form, text="Teléfono: ")
label_phone.grid(row=1, column=0, sticky="w", padx=(0,10), pady=(10,0))
input_phone = tk.Entry(frame_form, width=30)
input_phone.grid(row=1, column=1, padx=(0,20), pady=(10,0))

# Frame para botones
frame_buttons = tk.Frame(win)
frame_buttons.pack(pady=10)

btn_add = tk.Button(frame_buttons, text="AÑADIR", command=lambda: add_contact(), bg="green", fg="white")
btn_add.grid(row=0, column=0, padx=5)

btn_edit = tk.Button(frame_buttons, text="EDITAR", command=lambda: edit_contact(), bg="orange", fg="white")
btn_edit.grid(row=0, column=1, padx=5)

btn_delete = tk.Button(frame_buttons, text="ELIMINAR", command=lambda: delete_contact(), bg="red", fg="white")
btn_delete.grid(row=0, column=2, padx=5)

btn_restore = tk.Button(frame_buttons, text="RESTAURAR", command=lambda: restore_contact(), bg="blue", fg="white")
btn_restore.grid(row=0, column=3, padx=5)

btn_cancel = tk.Button(frame_buttons, text="CANCELAR", command=lambda: cancel_edit(), bg="gray", fg="white")
btn_cancel.grid(row=0, column=4, padx=5)

# Checkbox para mostrar eliminados
frame_filter = tk.Frame(win)
frame_filter.pack(pady=5)
check_show_deleted = tk.Checkbutton(frame_filter, text="Mostrar contactos eliminados", 
                                   variable=show_deleted, command=update_display)
check_show_deleted.pack()

# Treeview
tree_agenda = ttk.Treeview(win, columns=("id","name","phone","status"), show="headings", height=15)
tree_agenda.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

# Configurar columnas
tree_agenda.heading("id", text="ID")
tree_agenda.heading("name", text="NOMBRE")
tree_agenda.heading("phone", text="TELÉFONO")
tree_agenda.heading("status", text="ESTADO")

tree_agenda.column("id", anchor="center", width=50)
tree_agenda.column("name", anchor="center", width=200)
tree_agenda.column("phone", anchor="center", width=150)
tree_agenda.column("status", anchor="center", width=100)

# Vincular evento de doble clic
tree_agenda.bind("<Double-1>", on_double_click)

# Inicializar la visualización
update_display()

win.mainloop()
