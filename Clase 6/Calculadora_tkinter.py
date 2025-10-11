import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("🧮 Calculadora")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        # Variables para almacenar datos
        self.expresion = ""
        self.resultado_actual = ""
        self.operador_anterior = ""
        self.nuevo_numero = True
        
        # Configurar fuente personalizada
        self.configurar_fuentes()
        
        # Crear la pantalla de la calculadora
        self.crear_pantalla()
        
        # Crear los botones
        self.crear_botones()
        
        # Configurar eventos del teclado
        self.configurar_teclado()
    
    def configurar_fuentes(self):
        """Configurar fuentes personalizadas"""
        try:
            self.fuente_numeros = ("Segoe UI", 24, "bold")
            self.fuente_botones = ("Segoe UI", 14, "bold")
            self.fuente_operaciones = ("Segoe UI", 12)
        except:
            self.fuente_numeros = ("Arial", 24, "bold")
            self.fuente_botones = ("Arial", 14, "bold")
            self.fuente_operaciones = ("Arial", 12)
    
    def crear_pantalla(self):
        # Frame para la pantalla
        self.frame_pantalla = tk.Frame(self.root, bg="#ffffff", relief='sunken', bd=2)
        self.frame_pantalla.pack(fill="x", padx=10, pady=(10, 5))
        
        # Label para mostrar la operación actual
        self.pantalla_operacion = tk.Label(
            self.frame_pantalla, 
            text="", 
            font=self.fuente_operaciones, 
            bg="#ffffff", 
            fg="#666666", 
            anchor="e", 
            height=2
        )
        self.pantalla_operacion.pack(fill="x", padx=15, pady=(10, 0))
        
        # Entry principal para mostrar números
        frame_resultado = tk.Frame(self.frame_pantalla, bg="#ffffff")
        frame_resultado.pack(fill="x", padx=15, pady=(5, 15))
        
        self.pantalla = tk.Entry(
            frame_resultado, 
            font=self.fuente_numeros, 
            justify="right", 
            bg="white", 
            fg="black", 
            bd=0, 
            state="readonly", 
            relief="flat"
        )
        self.pantalla.pack(fill="x", ipady=10)
        
        # Inicializar con 0
        self.actualizar_pantalla("0")
    
    def crear_botones(self):
        # Frame para los botones
        frame_botones = tk.Frame(self.root, bg="#f0f0f0")
        frame_botones.pack(fill="both", expand=True, padx=10, pady=(5, 10))
        
        # Definir los botones
        botones = [
            [('C', '#9e9e9e'), ('CE', '#9e9e9e'), ('⌫', '#9e9e9e'), ('÷', '#4CAF50')],
            [('7', '#e8e8e8'), ('8', '#e8e8e8'), ('9', '#e8e8e8'), ('×', '#4CAF50')],
            [('4', '#e8e8e8'), ('5', '#e8e8e8'), ('6', '#e8e8e8'), ('-', '#4CAF50')],
            [('1', '#e8e8e8'), ('2', '#e8e8e8'), ('3', '#e8e8e8'), ('+', '#4CAF50')],
            [('±', '#9e9e9e'), ('0', '#e8e8e8'), ('.', '#e8e8e8'), ('=', '#4CAF50')]
        ]
        
        # Crear los botones
        for i, fila in enumerate(botones):
            for j, (valor, color) in enumerate(fila):
                boton = tk.Button(
                    frame_botones, 
                    text=valor, 
                    font=self.fuente_botones,
                    bg=color, 
                    fg="#333333", 
                    bd=1, 
                    relief="raised", 
                    cursor="hand2",
                    command=lambda v=valor: self.presionar_boton(v)
                )
                
                boton.grid(row=i, column=j, sticky="nsew", padx=2, pady=2, ipadx=5, ipady=5)
        
        # Configurar redimensionamiento
        for i in range(5):
            frame_botones.grid_rowconfigure(i, weight=1, minsize=60)
        for j in range(4):
            frame_botones.grid_columnconfigure(j, weight=1, minsize=80)
    
    def configurar_teclado(self):
        """Configurar eventos del teclado"""
        self.root.bind('<Key>', self.tecla_presionada)
        self.root.focus_set()
    
    def tecla_presionada(self, event):
        """Manejar teclas del teclado"""
        tecla = event.char
        if tecla in '0123456789':
            self.presionar_boton(tecla)
        elif tecla == '.':
            self.presionar_boton('.')
        elif tecla == '+':
            self.presionar_boton('+')
        elif tecla == '-':
            self.presionar_boton('-')
        elif tecla == '*':
            self.presionar_boton('×')
        elif tecla == '/':
            self.presionar_boton('÷')
        elif tecla == '\r' or tecla == '=':  # Enter o =
            self.presionar_boton('=')
        elif event.keysym == 'BackSpace':
            self.presionar_boton('⌫')
        elif event.keysym == 'Escape':
            self.presionar_boton('C')
    
    def presionar_boton(self, valor):
        if valor in '0123456789':
            self.agregar_numero(valor)
        elif valor == '.':
            self.agregar_punto()
        elif valor in ['+', '-', '×', '÷']:
            self.agregar_operador(valor)
        elif valor == '=':
            self.calcular()
        elif valor == 'C':
            self.limpiar_todo()
        elif valor == 'CE':
            self.limpiar_entrada()
        elif valor == '⌫':
            self.borrar_ultimo()
        elif valor == '±':
            self.cambiar_signo()
    
    def agregar_numero(self, numero):
        valor_actual = self.pantalla.get()
        if self.nuevo_numero or valor_actual == "0":
            self.actualizar_pantalla(numero)
            self.nuevo_numero = False
        else:
            self.actualizar_pantalla(valor_actual + numero)
    
    def agregar_punto(self):
        valor_actual = self.pantalla.get()
        if self.nuevo_numero:
            self.actualizar_pantalla("0.")
            self.nuevo_numero = False
        elif '.' not in valor_actual:
            self.actualizar_pantalla(valor_actual + '.')
    
    def agregar_operador(self, operador):
        valor_actual = self.pantalla.get()
        if not self.nuevo_numero and self.operador_anterior:
            # Si hay una operación pendiente, calcularla primero
            self.calcular()
            valor_actual = self.pantalla.get()
        
        self.resultado_actual = float(valor_actual)
        self.operador_anterior = operador
        self.nuevo_numero = True
        
        # Mostrar la operación en la pantalla superior
        simbolos = {'+': '+', '-': '-', '×': '×', '÷': '÷'}
        self.pantalla_operacion.config(text=f"{valor_actual} {simbolos[operador]}")
    
    def calcular(self):
        if self.operador_anterior and not self.nuevo_numero:
            try:
                valor_actual = float(self.pantalla.get())
                
                if self.operador_anterior == '+':
                    resultado = self.resultado_actual + valor_actual
                elif self.operador_anterior == '-':
                    resultado = self.resultado_actual - valor_actual
                elif self.operador_anterior == '×':
                    resultado = self.resultado_actual * valor_actual
                elif self.operador_anterior == '÷':
                    if valor_actual == 0:
                        messagebox.showerror("Error", "No se puede dividir por cero")
                        return
                    resultado = self.resultado_actual / valor_actual
                
                # Formatear el resultado
                if resultado == int(resultado):
                    resultado = int(resultado)
                
                self.actualizar_pantalla(str(resultado))
                self.pantalla_operacion.config(text="")
                self.operador_anterior = ""
                self.nuevo_numero = True
                
            except Exception as e:
                messagebox.showerror("Error", "Error en el cálculo")
                self.limpiar_todo()
    
    def limpiar_todo(self):
        self.expresion = ""
        self.resultado_actual = ""
        self.operador_anterior = ""
        self.nuevo_numero = True
        self.actualizar_pantalla("0")
        self.pantalla_operacion.config(text="")
    
    def limpiar_entrada(self):
        self.actualizar_pantalla("0")
        self.nuevo_numero = True
    
    def borrar_ultimo(self):
        valor_actual = self.pantalla.get()
        if len(valor_actual) > 1:
            nuevo_valor = valor_actual[:-1]
            self.actualizar_pantalla(nuevo_valor)
        else:
            self.actualizar_pantalla("0")
            self.nuevo_numero = True
    
    def cambiar_signo(self):
        valor_actual = self.pantalla.get()
        if valor_actual != "0":
            if valor_actual.startswith('-'):
                nuevo_valor = valor_actual[1:]
            else:
                nuevo_valor = '-' + valor_actual
            self.actualizar_pantalla(nuevo_valor)
    
    def actualizar_pantalla(self, texto):
        self.pantalla.config(state="normal")
        self.pantalla.delete(0, tk.END)
        self.pantalla.insert(0, texto)
        self.pantalla.config(state="readonly")

if __name__ == "__main__":
    root = tk.Tk()
    calculadora = Calculadora(root)
    root.mainloop()