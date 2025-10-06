import tkinter as tk
from tkinter import messagebox
import math
import json
import os

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("🧮 Calculadora Pro")
        self.root.geometry("600x700")  # Más grande para nuevas funciones
        self.root.resizable(False, False)
        
        # Quitar el icono de tkinter
        try:
            # Crear un icono invisible (1x1 píxel transparente)
            self.root.wm_attributes('-toolwindow', True)
            self.root.wm_attributes('-toolwindow', False)
        except:
            try:
                # Alternativa: usar iconphoto con imagen vacía
                self.root.iconphoto(False, tk.PhotoImage(width=1, height=1))
            except:
                pass
        
        # Variables para almacenar datos
        self.expresion = ""
        self.resultado_actual = ""
        self.operador_anterior = ""
        self.nuevo_numero = True
        self.historial = []
        
        # Sistema de temas
        self.tema_actual = "oscuro"
        self.inicializar_temas()
        
        # Configurar fuente personalizada
        self.configurar_fuentes()
        
        # Aplicar tema inicial
        self.aplicar_tema()
        
        # Crear marco principal con borde
        self.crear_marco_principal()
        
        # Crear barra de herramientas
        self.crear_barra_herramientas()
        
        # Crear layout principal
        self.crear_layout_principal()
        
        # Crear la pantalla de la calculadora
        self.crear_pantalla()
        
        # Crear los botones
        self.crear_botones()
        
        # Crear funciones avanzadas
        self.crear_funciones_avanzadas()
        
        # Crear historial
        self.crear_panel_historial()
        
        # Agregar efectos y animaciones
        self.configurar_efectos()
        
        # Animación de inicio comentada - se quitó la animación de apertura
        # self.animacion_apertura()
    
    def inicializar_temas(self):
        """Definir temas disponibles"""
        self.temas = {
            'oscuro': {
                'fondo_principal': '#0f0f0f',
                'fondo_pantalla': '#1a1a1a',
                'pantalla_fondo': 'white',
                'pantalla_texto': 'black',
                'pantalla_operacion': '#888888',
                'boton_numero': '#2d2d2d',
                'boton_numero_hover': '#3d3d3d',
                'boton_operador': '#ff9500',
                'boton_operador_hover': '#ffad33',
                'boton_funcion': '#505050',
                'boton_funcion_hover': '#606060',
                'boton_igual': '#ff9500',
                'boton_igual_hover': '#ffad33',
                'boton_avanzado': '#4a90e2',
                'boton_avanzado_hover': '#5ba0f2',
                'texto_boton': '#ffffff',
                'borde': '#333333',
                'barra_herramientas': '#1a1a1a'
            },
            'claro': {
                'fondo_principal': '#f0f0f0',
                'fondo_pantalla': '#ffffff',
                'pantalla_fondo': 'white',
                'pantalla_texto': 'black',
                'pantalla_operacion': '#666666',
                'boton_numero': '#e8e8e8',
                'boton_numero_hover': '#d8d8d8',
                'boton_operador': '#4CAF50',
                'boton_operador_hover': '#45a049',
                'boton_funcion': '#9e9e9e',
                'boton_funcion_hover': '#757575',
                'boton_igual': '#4CAF50',
                'boton_igual_hover': '#45a049',
                'boton_avanzado': '#2196F3',
                'boton_avanzado_hover': '#1976D2',
                'texto_boton': '#333333',
                'borde': '#cccccc',
                'barra_herramientas': '#ffffff'
            }
        }
    
    def configurar_fuentes(self):
        """Configurar fuentes personalizadas"""
        try:
            # Intentar usar fuentes más modernas
            self.fuente_numeros = ("Segoe UI", 24, "bold")
            self.fuente_botones = ("Segoe UI", 14, "bold")
            self.fuente_operaciones = ("Segoe UI", 12)
            self.fuente_titulo = ("Segoe UI", 10, "bold")
        except:
            # Fallback a fuentes por defecto
            self.fuente_numeros = ("Arial", 24, "bold")
            self.fuente_botones = ("Arial", 14, "bold")
            self.fuente_operaciones = ("Arial", 12)
            self.fuente_titulo = ("Arial", 10, "bold")
    
    def aplicar_tema(self):
        """Aplicar el tema actual"""
        self.colores = self.temas[self.tema_actual]
        self.root.configure(bg=self.colores['fondo_principal'])
    
    def alternar_tema(self):
        """Cambiar entre tema oscuro y claro"""
        self.tema_actual = "claro" if self.tema_actual == "oscuro" else "oscuro"
        self.aplicar_tema()
        self.actualizar_interfaz()
    
    def actualizar_interfaz(self):
        """Actualizar todos los elementos de la interfaz con el nuevo tema"""
        # Actualizar fondo principal
        self.root.configure(bg=self.colores['fondo_principal'])
        
        # Actualizar marcos
        if hasattr(self, 'marco_principal'):
            self.marco_principal.configure(bg=self.colores['borde'])
            self.marco_interior.configure(bg=self.colores['fondo_principal'])
        
        # Actualizar barra de herramientas
        if hasattr(self, 'barra_herramientas'):
            self.barra_herramientas.configure(bg=self.colores['barra_herramientas'])
            self.btn_tema.configure(
                bg=self.colores['boton_funcion'],
                activebackground=self.colores['boton_funcion_hover']
            )
        
        # Actualizar pantalla
        if hasattr(self, 'frame_pantalla'):
            self.frame_pantalla.configure(bg=self.colores['fondo_pantalla'])
            self.pantalla_operacion.configure(
                bg=self.colores['fondo_pantalla'],
                fg=self.colores['pantalla_operacion']
            )
            self.pantalla.configure(
                bg=self.colores['pantalla_fondo'],
                fg=self.colores['pantalla_texto']
            )
        
        # Actualizar botones
        self.actualizar_botones_tema()
        
        # Actualizar historial
        if hasattr(self, 'frame_historial'):
            self.frame_historial.configure(bg=self.colores['fondo_pantalla'])
            self.lista_historial.configure(
                bg=self.colores['pantalla_fondo'],
                fg=self.colores['pantalla_texto']
            )
    
    def crear_marco_principal(self):
        """Crear marco principal con borde y sombra"""
        self.marco_principal = tk.Frame(self.root, bg=self.colores['borde'], bd=2, relief='raised')
        self.marco_principal.pack(fill='both', expand=True, padx=8, pady=8)
        
        self.marco_interior = tk.Frame(self.marco_principal, bg=self.colores['fondo_principal'])
        self.marco_interior.pack(fill='both', expand=True, padx=2, pady=2)
    
    def crear_barra_herramientas(self):
        """Crear barra de herramientas con botón de tema"""
        self.barra_herramientas = tk.Frame(self.marco_interior, bg=self.colores['barra_herramientas'], height=40)
        self.barra_herramientas.pack(fill='x', padx=5, pady=(5, 0))
        self.barra_herramientas.pack_propagate(False)
        
        # Botón para cambiar tema
        tema_texto = "☀️ Claro" if self.tema_actual == "oscuro" else "🌙 Oscuro"
        self.btn_tema = tk.Button(
            self.barra_herramientas,
            text=tema_texto,
            font=self.fuente_titulo,
            bg=self.colores['boton_funcion'],
            fg=self.colores['texto_boton'],
            bd=0,
            relief="flat",
            cursor="hand2",
            command=self.alternar_tema
        )
        self.btn_tema.pack(side='right', padx=5, pady=5)
        
        # Título
        titulo_label = tk.Label(
            self.barra_herramientas,
            text="🧮 Calculadora Pro",
            font=self.fuente_titulo,
            bg=self.colores['barra_herramientas'],
            fg=self.colores['pantalla_operacion']
        )
        titulo_label.pack(side='left', padx=10, pady=5)
    
    def crear_layout_principal(self):
        """Crear el layout principal con calculadora e historial"""
        # Frame principal que contiene calculadora e historial
        self.frame_contenido = tk.Frame(self.marco_interior, bg=self.colores['fondo_principal'])
        self.frame_contenido.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Frame izquierdo para la calculadora
        self.frame_calculadora = tk.Frame(self.frame_contenido, bg=self.colores['fondo_principal'])
        self.frame_calculadora.pack(side='left', fill='both', expand=True, padx=(0, 5))
        
        # Frame derecho para el historial
        self.frame_historial_container = tk.Frame(self.frame_contenido, bg=self.colores['fondo_pantalla'], width=200)
        self.frame_historial_container.pack(side='right', fill='y', padx=(5, 0))
        self.frame_historial_container.pack_propagate(False)
    
    def crear_pantalla(self):
        # Frame para la pantalla con efectos
        self.frame_pantalla = tk.Frame(self.frame_calculadora, bg=self.colores['fondo_pantalla'], 
                                      relief='sunken', bd=2)
        self.frame_pantalla.pack(fill="x", padx=10, pady=(10, 5))
        
        # Label para mostrar la operación actual con estilo
        self.pantalla_operacion = tk.Label(self.frame_pantalla, text="", font=self.fuente_operaciones, 
                                          bg=self.colores['fondo_pantalla'], 
                                          fg=self.colores['pantalla_operacion'], 
                                          anchor="e", height=2)
        self.pantalla_operacion.pack(fill="x", padx=15, pady=(10, 0))
        
        # Entry principal con fondo blanco y texto negro
        frame_resultado = tk.Frame(self.frame_pantalla, bg=self.colores['fondo_pantalla'])
        frame_resultado.pack(fill="x", padx=15, pady=(5, 15))
        
        self.pantalla = tk.Entry(frame_resultado, font=self.fuente_numeros, justify="right", 
                                bg=self.colores['pantalla_fondo'], fg=self.colores['pantalla_texto'], 
                                bd=0, state="readonly", relief="flat", 
                                insertbackground=self.colores['pantalla_texto'],
                                highlightthickness=2, highlightcolor=self.colores['boton_operador'])
        self.pantalla.pack(fill="x", ipady=10)
        
        # Inicializar con 0
        self.actualizar_pantalla("0")
    
    def crear_botones(self):
        # Frame para los botones con mejor espaciado
        frame_botones = tk.Frame(self.frame_calculadora, bg=self.colores['fondo_principal'])
        frame_botones.pack(fill="both", expand=True, padx=10, pady=(5, 5))
        
        # Definir los botones con más detalles de estilo
        botones = [
            [('C', 'funcion', '🗑️'), ('CE', 'funcion', '↶'), ('⌫', 'funcion', '⌫'), ('÷', 'operador', '÷')],
            [('7', 'numero', '7'), ('8', 'numero', '8'), ('9', 'numero', '9'), ('×', 'operador', '×')],
            [('4', 'numero', '4'), ('5', 'numero', '5'), ('6', 'numero', '6'), ('-', 'operador', '−')],
            [('1', 'numero', '1'), ('2', 'numero', '2'), ('3', 'numero', '3'), ('+', 'operador', '+')],
            [('±', 'funcion', '±'), ('0', 'numero', '0'), ('.', 'numero', '•'), ('=', 'igual', '=')]
        ]
        
        # Crear los botones con efectos avanzados
        self.botones_refs = []
        for i, fila in enumerate(botones):
            fila_botones = []
            for j, (valor, tipo, simbolo) in enumerate(fila):
                # Determinar colores según el tipo
                if tipo == 'numero':
                    bg_color = self.colores['boton_numero']
                    hover_color = self.colores['boton_numero_hover']
                elif tipo == 'operador':
                    bg_color = self.colores['boton_operador']
                    hover_color = self.colores['boton_operador_hover']
                elif tipo == 'igual':
                    bg_color = self.colores['boton_igual']
                    hover_color = self.colores['boton_igual_hover']
                else:  # funcion
                    bg_color = self.colores['boton_funcion']
                    hover_color = self.colores['boton_funcion_hover']
                
                # Crear botón con efectos
                boton = tk.Button(frame_botones, text=simbolo, font=("Segoe UI", 18, "bold"),
                                bg=bg_color, fg=self.colores['texto_boton'], 
                                bd=0, relief="raised", cursor="hand2",
                                activebackground=hover_color, 
                                activeforeground=self.colores['texto_boton'],
                                command=lambda v=valor: self.presionar_boton(v))
                
                boton.grid(row=i, column=j, sticky="nsew", padx=3, pady=3, ipadx=5, ipady=5)
                
                # Agregar efectos hover y click
                self.agregar_efectos_boton(boton, bg_color, hover_color, tipo)
                fila_botones.append(boton)
            
            self.botones_refs.append(fila_botones)
        
        # Configurar redimensionamiento
        for i in range(5):
            frame_botones.grid_rowconfigure(i, weight=1, minsize=55)
        for j in range(4):
            frame_botones.grid_columnconfigure(j, weight=1, minsize=70)
    
    def crear_funciones_avanzadas(self):
        """Crear panel de funciones matemáticas avanzadas"""
        # Frame para funciones avanzadas
        frame_avanzadas = tk.Frame(self.frame_calculadora, bg=self.colores['fondo_principal'])
        frame_avanzadas.pack(fill="x", padx=10, pady=(5, 10))
        
        # Botones de funciones avanzadas
        funciones = [
            [('√', 'sqrt'), ('x²', 'square'), ('x³', 'cube'), ('xʸ', 'power')],
            [('sin', 'sin'), ('cos', 'cos'), ('tan', 'tan'), ('π', 'pi')],
            [('log', 'log'), ('ln', 'ln'), ('e', 'e'), ('1/x', 'reciprocal')]
        ]
        
        self.botones_avanzados = []
        for i, fila in enumerate(funciones):
            fila_botones = []
            for j, (texto, funcion) in enumerate(fila):
                boton = tk.Button(frame_avanzadas, text=texto, font=("Segoe UI", 10, "bold"),
                                bg=self.colores['boton_avanzado'], fg=self.colores['texto_boton'], 
                                bd=0, relief="raised", cursor="hand2",
                                activebackground=self.colores['boton_avanzado_hover'], 
                                activeforeground=self.colores['texto_boton'],
                                command=lambda f=funcion: self.funcion_avanzada(f))
                
                boton.grid(row=i, column=j, sticky="nsew", padx=1, pady=1, ipadx=2, ipady=2)
                
                # Agregar efectos hover
                self.agregar_efectos_boton(boton, 
                                         self.colores['boton_avanzado'], 
                                         self.colores['boton_avanzado_hover'], 
                                         'avanzado')
                fila_botones.append(boton)
            
            self.botones_avanzados.append(fila_botones)
        
        # Configurar redimensionamiento
        for i in range(3):
            frame_avanzadas.grid_rowconfigure(i, weight=1, minsize=35)
        for j in range(4):
            frame_avanzadas.grid_columnconfigure(j, weight=1)
    
    def crear_panel_historial(self):
        """Crear panel lateral para mostrar el historial"""
        # Título del historial
        titulo_historial = tk.Label(
            self.frame_historial_container,
            text="📊 Historial",
            font=self.fuente_titulo,
            bg=self.colores['fondo_pantalla'],
            fg=self.colores['pantalla_operacion']
        )
        titulo_historial.pack(pady=(10, 5))
        
        # Frame para la lista del historial
        self.frame_historial = tk.Frame(self.frame_historial_container, bg=self.colores['fondo_pantalla'])
        self.frame_historial.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Lista del historial con scroll
        frame_lista = tk.Frame(self.frame_historial, bg=self.colores['pantalla_fondo'])
        frame_lista.pack(fill='both', expand=True)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(frame_lista)
        scrollbar.pack(side='right', fill='y')
        
        # Listbox para el historial
        self.lista_historial = tk.Listbox(
            frame_lista,
            font=("Consolas", 9),
            bg=self.colores['pantalla_fondo'],
            fg=self.colores['pantalla_texto'],
            selectbackground=self.colores['boton_operador'],
            bd=0,
            yscrollcommand=scrollbar.set,
            activestyle='none'
        )
        self.lista_historial.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=self.lista_historial.yview)
        
        # Botón para limpiar historial
        btn_limpiar_historial = tk.Button(
            self.frame_historial_container,
            text="🗑️ Limpiar",
            font=("Segoe UI", 9),
            bg=self.colores['boton_funcion'],
            fg=self.colores['texto_boton'],
            bd=0,
            relief="flat",
            cursor="hand2",
            command=self.limpiar_historial
        )
        btn_limpiar_historial.pack(pady=(5, 10))
        
        # Evento para usar elemento del historial
        self.lista_historial.bind('<Double-Button-1>', self.usar_del_historial)
    
    def agregar_efectos_boton(self, boton, color_normal, color_hover, tipo):
        """Agregar efectos visuales a los botones"""
        def on_enter(e):
            boton.configure(bg=color_hover, relief="raised")
            if tipo == 'operador' or tipo == 'igual':
                boton.configure(font=("Segoe UI", 19, "bold"))
        
        def on_leave(e):
            boton.configure(bg=color_normal, relief="raised")
            boton.configure(font=("Segoe UI", 18, "bold"))
        
        def on_click(e):
            boton.configure(relief="sunken")
            self.root.after(100, lambda: boton.configure(relief="raised"))
        
        boton.bind("<Enter>", on_enter)
        boton.bind("<Leave>", on_leave)
        boton.bind("<Button-1>", on_click)
    
    def configurar_efectos(self):
        """Configurar efectos adicionales"""
        # Efecto de parpadeo en la pantalla cuando hay error
        self.pantalla_normal_bg = self.pantalla.cget('bg')
        
        # Configurar teclas del teclado (mejoradas)
        self.root.bind('<Key>', self.tecla_presionada)
        self.root.bind('<Control-c>', self.copiar_resultado)
        self.root.bind('<Control-v>', self.pegar_numero)
        self.root.bind('<Escape>', self.cerrar_app)
        self.root.bind('<F1>', self.mostrar_ayuda)
        self.root.focus_set()
        
        # Animación inicial
        self.root.after(100, self.animacion_inicio)
    
    def animacion_apertura(self):
        """Animación de apertura de la ventana"""
        # Empezar pequeño y crecer
        self.root.geometry("200x200")
        self.root.update()
        
        # Animación gradual
        for size in range(200, 700, 50):
            width = min(size * 0.85, 600)  # Mantener proporción
            height = size
            self.root.geometry(f"{int(width)}x{height}")
            self.root.update()
            self.root.after(30)
    
    def funcion_avanzada(self, funcion):
        """Ejecutar funciones matemáticas avanzadas"""
        try:
            valor_actual = float(self.pantalla.get())
            resultado = None
            operacion_texto = ""
            
            if funcion == 'sqrt':
                if valor_actual < 0:
                    raise ValueError("No se puede calcular raíz cuadrada de número negativo")
                resultado = math.sqrt(valor_actual)
                operacion_texto = f"√{valor_actual}"
            elif funcion == 'square':
                resultado = valor_actual ** 2
                operacion_texto = f"{valor_actual}²"
            elif funcion == 'cube':
                resultado = valor_actual ** 3
                operacion_texto = f"{valor_actual}³"
            elif funcion == 'sin':
                resultado = math.sin(math.radians(valor_actual))
                operacion_texto = f"sin({valor_actual}°)"
            elif funcion == 'cos':
                resultado = math.cos(math.radians(valor_actual))
                operacion_texto = f"cos({valor_actual}°)"
            elif funcion == 'tan':
                resultado = math.tan(math.radians(valor_actual))
                operacion_texto = f"tan({valor_actual}°)"
            elif funcion == 'log':
                if valor_actual <= 0:
                    raise ValueError("Logaritmo de número negativo o cero")
                resultado = math.log10(valor_actual)
                operacion_texto = f"log({valor_actual})"
            elif funcion == 'ln':
                if valor_actual <= 0:
                    raise ValueError("Logaritmo natural de número negativo o cero")
                resultado = math.log(valor_actual)
                operacion_texto = f"ln({valor_actual})"
            elif funcion == 'reciprocal':
                if valor_actual == 0:
                    raise ValueError("División por cero")
                resultado = 1 / valor_actual
                operacion_texto = f"1/{valor_actual}"
            elif funcion == 'pi':
                resultado = math.pi
                operacion_texto = "π"
            elif funcion == 'e':
                resultado = math.e
                operacion_texto = "e"
            
            if resultado is not None:
                # Formatear resultado
                if abs(resultado) < 1e-10:
                    resultado = 0
                elif resultado == int(resultado):
                    resultado = int(resultado)
                
                # Agregar al historial
                self.agregar_al_historial(operacion_texto, resultado)
                
                # Mostrar resultado
                self.actualizar_pantalla(str(resultado))
                self.pantalla_operacion.config(text=operacion_texto + " =")
                self.nuevo_numero = True
                
        except Exception as e:
            messagebox.showerror("Error", f"Error en función matemática: {str(e)}")
            self.efecto_error()
    
    def copiar_resultado(self, event=None):
        """Copiar el resultado actual al portapapeles"""
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.pantalla.get())
            self.pantalla_operacion.config(text="📋 Copiado al portapapeles")
            self.root.after(2000, lambda: self.pantalla_operacion.config(text=""))
        except:
            pass
    
    def pegar_numero(self, event=None):
        """Pegar número del portapapeles"""
        try:
            texto = self.root.clipboard_get()
            # Validar que sea un número
            float(texto)
            self.actualizar_pantalla(texto)
            self.nuevo_numero = True
        except:
            messagebox.showerror("Error", "El contenido del portapapeles no es un número válido")
    
    def cerrar_app(self, event=None):
        """Cerrar la aplicación"""
        self.root.quit()
    
    def mostrar_ayuda(self, event=None):
        """Mostrar ayuda de atajos de teclado"""
        ayuda = """🔹 ATAJOS DE TECLADO 🔹
        
Números: 0-9
Operaciones: +, -, *, /
Decimal: . (punto)
Calcular: Enter o =
Borrar último: Backspace
Limpiar todo: Escape
Copiar resultado: Ctrl+C
Pegar número: Ctrl+V
Cambiar tema: Botón en barra
Ayuda: F1

🔹 FUNCIONES AVANZADAS 🔹
√ - Raíz cuadrada
x² - Potencia al cuadrado  
x³ - Potencia al cubo
sin, cos, tan - Trigonometría (grados)
log, ln - Logaritmos
1/x - Recíproco
π, e - Constantes matemáticas

🔹 HISTORIAL 🔹
Doble clic en elemento para usarlo"""
        
        messagebox.showinfo("Ayuda - Calculadora Pro", ayuda)
    
    def agregar_al_historial(self, operacion, resultado):
        """Agregar operación al historial"""
        entrada = f"{operacion} = {resultado}"
        self.historial.append(entrada)
        self.lista_historial.insert(0, entrada)  # Agregar al inicio
        
        # Limitar historial a 50 elementos
        if len(self.historial) > 50:
            self.historial.pop()
            self.lista_historial.delete(50)
    
    def limpiar_historial(self):
        """Limpiar todo el historial"""
        self.historial.clear()
        self.lista_historial.delete(0, tk.END)
    
    def usar_del_historial(self, event):
        """Usar un elemento del historial (doble clic)"""
        try:
            seleccion = self.lista_historial.curselection()
            if seleccion:
                entrada = self.lista_historial.get(seleccion[0])
                # Extraer solo el resultado (después del =)
                resultado = entrada.split(' = ')[-1]
                self.actualizar_pantalla(resultado)
                self.nuevo_numero = True
        except:
            pass
    
    def actualizar_botones_tema(self):
        """Actualizar colores de todos los botones al cambiar tema"""
        if hasattr(self, 'botones_refs'):
            tipos_botones = [
                [('C', 'funcion'), ('CE', 'funcion'), ('⌫', 'funcion'), ('÷', 'operador')],
                [('7', 'numero'), ('8', 'numero'), ('9', 'numero'), ('×', 'operador')],
                [('4', 'numero'), ('5', 'numero'), ('6', 'numero'), ('-', 'operador')],
                [('1', 'numero'), ('2', 'numero'), ('3', 'numero'), ('+', 'operador')],
                [('±', 'funcion'), ('0', 'numero'), ('.', 'numero'), ('=', 'igual')]
            ]
            
            for i, fila in enumerate(self.botones_refs):
                for j, boton in enumerate(fila):
                    _, tipo = tipos_botones[i][j]
                    if tipo == 'numero':
                        bg_color = self.colores['boton_numero']
                        hover_color = self.colores['boton_numero_hover']
                    elif tipo == 'operador':
                        bg_color = self.colores['boton_operador']
                        hover_color = self.colores['boton_operador_hover']
                    elif tipo == 'igual':
                        bg_color = self.colores['boton_igual']
                        hover_color = self.colores['boton_igual_hover']
                    else:  # funcion
                        bg_color = self.colores['boton_funcion']
                        hover_color = self.colores['boton_funcion_hover']
                    
                    boton.configure(
                        bg=bg_color,
                        fg=self.colores['texto_boton'],
                        activebackground=hover_color
                    )
        
        # Actualizar botones avanzados
        if hasattr(self, 'botones_avanzados'):
            for fila in self.botones_avanzados:
                for boton in fila:
                    boton.configure(
                        bg=self.colores['boton_avanzado'],
                        fg=self.colores['texto_boton'],
                        activebackground=self.colores['boton_avanzado_hover']
                    )
        
        # Actualizar botón de tema
        tema_texto = "☀️ Claro" if self.tema_actual == "oscuro" else "🌙 Oscuro"
        self.btn_tema.configure(text=tema_texto)
    
    def animacion_inicio(self):
        """Pequeña animación al iniciar"""
        self.pantalla_operacion.config(text="✨ Lista para calcular ✨")
        self.root.after(2000, lambda: self.pantalla_operacion.config(text=""))
    
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
    
    def efecto_error(self):
        """Efecto visual para errores"""
        original_bg = self.pantalla.cget('bg')
        self.pantalla.config(bg='#ff4444')
        self.root.after(200, lambda: self.pantalla.config(bg=self.colores['pantalla_fondo']))
    
    def oscurecer_color(self, color):
        """Oscurece un color para el efecto hover"""
        return self.colores.get(f"{color}_hover", '#404040')
    
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
                        self.efecto_error()
                        return
                    resultado = self.resultado_actual / valor_actual
                
                # Formatear el resultado
                if resultado == int(resultado):
                    resultado = int(resultado)
                
                # Agregar al historial
                simbolos = {'+': '+', '-': '-', '×': '×', '÷': '÷'}
                operacion_completa = f"{self.resultado_actual} {simbolos[self.operador_anterior]} {valor_actual}"
                self.agregar_al_historial(operacion_completa, resultado)
                
                self.actualizar_pantalla(str(resultado))
                self.pantalla_operacion.config(text="")
                self.operador_anterior = ""
                self.nuevo_numero = True
                
            except Exception as e:
                messagebox.showerror("Error", "Error en el cálculo")
                self.efecto_error()
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
