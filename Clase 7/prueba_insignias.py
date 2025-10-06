import tkinter as tk
from tkinter import ttk, messagebox
import random
import os
from PIL import Image, ImageTk

# Prueba rápida para conseguir insignias
class PruebaInsignias:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Prueba de Insignias")
        self.root.geometry("600x400")
        self.root.configure(bg="#2E3440")
        
        # Simular datos del juego
        self.insignias_j1 = {"IA", "Programacion"}  # Simular 2 insignias ya obtenidas
        self.modo_juego = "single"
        
        # Cargar iconos
        self.iconos_path = {
            "IA": "img/pngtree-ai-icon-png-image_15382528.png",
            "Ciberseguridad": "img/ciberseguridad.png", 
            "Programacion": "img/programacion.png",
            "Redes": "img/redes.png"
        }
        
        self.iconos = {}
        self.iconos_refs = []
        self.cargar_iconos()
        
        # Crear interfaz
        self.crear_interfaz()
    
    def cargar_iconos(self):
        print("🔍 Cargando iconos para prueba...")
        try:
            for categoria, path in self.iconos_path.items():
                if os.path.exists(path):
                    imagen = Image.open(path)
                    imagen = imagen.resize((50, 50), Image.Resampling.LANCZOS)
                    photo = ImageTk.PhotoImage(imagen)
                    self.iconos[categoria] = photo
                    self.iconos_refs.append(photo)
                    print(f"✅ {categoria} cargado")
                else:
                    self.iconos[categoria] = None
                    print(f"❌ {categoria} no encontrado")
        except Exception as e:
            print(f"Error: {e}")
    
    def crear_interfaz(self):
        # Título
        titulo = tk.Label(self.root, text="🧪 PRUEBA DE INSIGNIAS", 
                         font=("Arial", 20, "bold"), fg="#81A1C1", bg="#2E3440")
        titulo.pack(pady=20)
        
        # Frame para insignias
        self.frame_insignias = tk.Frame(self.root, bg="#434C5E", relief="ridge", bd=2)
        self.frame_insignias.pack(pady=20, padx=20, fill="x")
        
        # Título insignias
        tk.Label(self.frame_insignias, text="🏆 Insignias Obtenidas:", 
                font=("Arial", 14, "bold"), fg="#EBCB8B", bg="#434C5E").pack(pady=10)
        
        # Frame para iconos
        self.frame_iconos = tk.Frame(self.frame_insignias, bg="#434C5E")
        self.frame_iconos.pack(pady=10)
        
        self.mostrar_insignias()
        
        # Botón para agregar insignia
        tk.Button(self.root, text="🎯 Agregar Insignia de Ciberseguridad", 
                 font=("Arial", 12, "bold"), bg="#A3BE8C", fg="white",
                 padx=20, pady=10, command=self.agregar_insignia).pack(pady=20)
        
        # Info
        info = tk.Label(self.root, text="Insignias actuales: IA, Programación", 
                       font=("Arial", 11), fg="#D8DEE9", bg="#2E3440")
        info.pack(pady=10)
    
    def mostrar_insignias(self):
        # Limpiar
        for widget in self.frame_iconos.winfo_children():
            widget.destroy()
        
        print(f"🏆 Mostrando insignias: {self.insignias_j1}")
        
        if self.insignias_j1:
            for categoria in ["IA", "Ciberseguridad", "Programacion", "Redes"]:
                if categoria in self.insignias_j1:
                    if self.iconos[categoria]:
                        # Frame contenedor
                        container = tk.Frame(self.frame_iconos, bg="#2E3440", relief="ridge", bd=2)
                        container.pack(side="left", padx=10, pady=5)
                        
                        # Icono
                        icono_label = tk.Label(container, image=self.iconos[categoria], bg="#2E3440")
                        icono_label.pack(pady=5)
                        
                        # Nombre
                        tk.Label(container, text=categoria, font=("Arial", 10, "bold"), 
                               fg="#ECEFF4", bg="#2E3440").pack(pady=(0, 5))
                        
                        print(f"✅ Mostrando icono para {categoria}")
                    else:
                        print(f"❌ No hay icono para {categoria}")
        else:
            tk.Label(self.frame_iconos, text="Sin insignias", 
                    font=("Arial", 12), fg="#D8DEE9", bg="#434C5E").pack()
    
    def agregar_insignia(self):
        print("🎉 Agregando insignia de Ciberseguridad...")
        self.insignias_j1.add("Ciberseguridad")
        self.mostrar_insignias()
        print(f"📋 Insignias actuales: {self.insignias_j1}")
    
    def ejecutar(self):
        self.root.mainloop()

if __name__ == "__main__":
    prueba = PruebaInsignias()
    prueba.ejecutar()