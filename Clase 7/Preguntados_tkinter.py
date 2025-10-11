import tkinter as tk
from tkinter import ttk, messagebox, Canvas
import random
import os
import math
from PIL import Image, ImageTk

class PreguntadosGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🎯 PREGUNTADOS - Trivia Game")
        self.root.geometry("800x600")
        self.root.configure(bg="#1a1a2e")
        self.root.resizable(True, True)  # Permitir redimensionar
        
        # Centrar ventana en la pantalla
        self.centrar_ventana()
        
        # Paleta de colores del Preguntados original
        self.colores = {
            "fondo_principal": "#1a1a2e",
            "fondo_secundario": "#16213e", 
            "fondo_tarjeta": "#0f3460",
            "texto_principal": "#ffffff",
            "texto_secundario": "#e94560",
            "boton_principal": "#e94560",
            "boton_secundario": "#0f3460",
            "verde_correcto": "#00d4aa",
            "rojo_incorrecto": "#ff6b6b",
            "amarillo_insignia": "#ffd93d",
            "azul_claro": "#6bcaff",
            # Colores de categorías (como la ruleta original)
            "IA": "#ff6b9d",           # Rosa
            "Ciberseguridad": "#4ecdc4", # Turquesa  
            "Programacion": "#45b7d1",   # Azul
            "Redes": "#f9ca24"          # Amarillo
        }
        
        # Variables del juego
        self.modo_juego = None  # "single" o "multiplayer"
        self.jugador_actual = 1
        self.puntuacion_j1 = 0
        self.puntuacion_j2 = 0
        self.respuestas_correctas_j1 = {"IA": 0, "Ciberseguridad": 0, "Programacion": 0, "Redes": 0}
        self.respuestas_correctas_j2 = {"IA": 0, "Ciberseguridad": 0, "Programacion": 0, "Redes": 0}
        self.insignias_j1 = set()
        self.insignias_j2 = set()
        self.pregunta_actual = None
        self.categoria_actual = None
        self.preguntas_usadas = set()
        
        # Mapeo de iconos por categoría - usando rutas absolutas
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.iconos_path = {
            "IA": os.path.join(script_dir, "img", "pngtree-ai-icon-png-image_15382528.png"),
            "Ciberseguridad": os.path.join(script_dir, "img", "ciberseguridad.png"), 
            "Programacion": os.path.join(script_dir, "img", "programacion.png"),
            "Redes": os.path.join(script_dir, "img", "redes.png")
        }
        
        # Cargar iconos
        self.iconos = {}
        self.iconos_refs = []  # Referencias persistentes para evitar garbage collection
        self.cargar_iconos()
        
        # Banco de preguntas
        self.preguntas = {
            "IA": [
                {
                    "pregunta": "¿Qué significa 'Machine Learning'?",
                    "opciones": ["Aprendizaje Automático", "Máquina de Aprender", "Aprendizaje Manual", "Inteligencia Humana"],
                    "respuesta_correcta": 0
                },
                {
                    "pregunta": "¿Cuál es el padre de la Inteligencia Artificial?",
                    "opciones": ["Alan Turing", "John McCarthy", "Marvin Minsky", "Herbert Simon"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué es una red neuronal artificial?",
                    "opciones": ["Un tipo de virus", "Un modelo matemático inspirado en el cerebro", "Un cable de red", "Un programa antivirus"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué significa 'Deep Learning'?",
                    "opciones": ["Aprendizaje Superficial", "Aprendizaje Profundo", "Aprendizaje Rápido", "Aprendizaje Lento"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Cuál es un ejemplo de procesamiento de lenguaje natural?",
                    "opciones": ["Reconocimiento de imágenes", "Traducción automática", "Juegos de video", "Cálculos matemáticos"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué es un algoritmo de clasificación?",
                    "opciones": ["Un método para organizar datos", "Un tipo de red neuronal", "Una técnica para categorizar datos", "Un lenguaje de programación"],
                    "respuesta_correcta": 2
                },
                {
                    "pregunta": "¿Cuál de estos es un framework de Machine Learning?",
                    "opciones": ["TensorFlow", "Photoshop", "Microsoft Word", "Chrome"],
                    "respuesta_correcta": 0
                },
                {
                    "pregunta": "¿Qué es el overfitting en Machine Learning?",
                    "opciones": ["Cuando el modelo es muy simple", "Cuando el modelo se ajusta demasiado a los datos de entrenamiento", "Cuando faltan datos", "Cuando el algoritmo es muy rápido"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué significa 'Big Data'?",
                    "opciones": ["Datos pequeños", "Grandes volúmenes de datos", "Datos rápidos", "Datos seguros"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Cuál es la diferencia entre IA supervisada y no supervisada?",
                    "opciones": ["No hay diferencia", "Supervisada usa datos etiquetados, no supervisada no", "Supervisada es más rápida", "No supervisada es más cara"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué es un chatbot?",
                    "opciones": ["Un robot físico", "Un programa que simula conversación humana", "Un tipo de virus", "Un navegador web"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Cuál es el Test de Turing?",
                    "opciones": ["Una prueba de velocidad", "Una prueba para determinar si una máquina puede exhibir comportamiento inteligente", "Un examen de programación", "Una prueba de memoria"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué es Computer Vision?",
                    "opciones": ["Visión humana mejorada", "Capacidad de las computadoras para interpretar imágenes", "Un tipo de pantalla", "Un programa de diseño"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Cuál de estos es un algoritmo de clustering?",
                    "opciones": ["K-means", "HTML", "CSS", "HTTP"],
                    "respuesta_correcta": 0
                },
                {
                    "pregunta": "¿Qué significa 'Reinforcement Learning'?",
                    "opciones": ["Aprendizaje por refuerzo", "Aprendizaje débil", "Aprendizaje rápido", "Aprendizaje manual"],
                    "respuesta_correcta": 0
                }
            ],
            "Ciberseguridad": [
                {
                    "pregunta": "¿Qué es un firewall?",
                    "opciones": ["Un tipo de virus", "Una barrera de seguridad", "Un navegador web", "Un antivirus"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué significa 'phishing'?",
                    "opciones": ["Pescar", "Robo de identidad digital", "Programar", "Hackear"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué es un malware?",
                    "opciones": ["Software malicioso", "Hardware dañado", "Un tipo de red", "Un lenguaje de programación"],
                    "respuesta_correcta": 0
                },
                {
                    "pregunta": "¿Qué es la autenticación de dos factores?",
                    "opciones": ["Una contraseña", "Dos métodos de verificación", "Un antivirus", "Un tipo de encriptación"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué significa 'DDoS'?",
                    "opciones": ["Ataque de Denegación de Servicio Distribuido", "Disco Duro de Datos", "Red de Datos", "Sistema Operativo"],
                    "respuesta_correcta": 0
                },
                {
                    "pregunta": "¿Qué es un virus informático?",
                    "opciones": ["Un programa que se replica y causa daños", "Un tipo de bacteria", "Un error de programación", "Un componente de hardware"],
                    "respuesta_correcta": 0
                },
                {
                    "pregunta": "¿Qué significa 'ransomware'?",
                    "opciones": ["Software gratuito", "Malware que secuestra datos por dinero", "Un tipo de firewall", "Un antivirus premium"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué es la criptografía?",
                    "opciones": ["Estudio de virus", "Técnica para proteger información mediante códigos", "Análisis de redes", "Programación de juegos"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué es un certificado SSL?",
                    "opciones": ["Un documento de identidad", "Un protocolo para conexiones seguras", "Un tipo de virus", "Un lenguaje de programación"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué significa 'spoofing'?",
                    "opciones": ["Acelerar conexiones", "Falsificar identidad en redes", "Comprimir archivos", "Instalar software"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué es un keylogger?",
                    "opciones": ["Un programa que registra pulsaciones de teclas", "Un tipo de teclado", "Un juego", "Un navegador web"],
                    "respuesta_correcta": 0
                },
                {
                    "pregunta": "¿Qué es el social engineering?",
                    "opciones": ["Ingeniería social", "Manipulación psicológica para obtener información", "Redes sociales", "Programación colaborativa"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué significa 'zero-day'?",
                    "opciones": ["Día cero", "Vulnerabilidad no conocida públicamente", "Primer día de trabajo", "Error sin importancia"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué es un honeypot?",
                    "opciones": ["Un tipo de miel", "Trampa para detectar ataques", "Un puerto de red", "Un protocolo de seguridad"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué es la autenticación biométrica?",
                    "opciones": ["Uso de características físicas únicas", "Contraseñas numéricas", "Códigos QR", "Tarjetas magnéticas"],
                    "respuesta_correcta": 0
                }
            ],
            "Programacion": [
                {
                    "pregunta": "¿Qué es Python?",
                    "opciones": ["Una serpiente", "Un lenguaje de programación", "Un sistema operativo", "Un navegador"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué significa 'HTML'?",
                    "opciones": ["HyperText Markup Language", "High Tech Modern Language", "Home Tool Markup Language", "Hard Text Making Language"],
                    "respuesta_correcta": 0
                },
                {
                    "pregunta": "¿Cuál es un paradigma de programación?",
                    "opciones": ["Orientado a objetos", "Orientado a sujetos", "Orientado a verbos", "Orientado a adjetivos"],
                    "respuesta_correcta": 0
                },
                {
                    "pregunta": "¿Qué es un algoritmo?",
                    "opciones": ["Un tipo de dato", "Una secuencia de pasos para resolver un problema", "Un lenguaje", "Un compilador"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué significa 'API'?",
                    "opciones": ["Application Programming Interface", "Advanced Programming Intelligence", "Automatic Program Installation", "Applied Programming Integration"],
                    "respuesta_correcta": 0
                },
                {
                    "pregunta": "¿Qué es una variable en programación?",
                    "opciones": ["Un valor constante", "Un espacio de memoria para almacenar datos", "Un tipo de función", "Un error de código"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Cuál de estos es un lenguaje de programación?",
                    "opciones": ["Photoshop", "JavaScript", "Microsoft Word", "Google Chrome"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué es un bucle 'for'?",
                    "opciones": ["Un tipo de variable", "Una estructura de repetición", "Una función matemática", "Un error de sintaxis"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué significa 'debugging'?",
                    "opciones": ["Escribir código", "Encontrar y corregir errores", "Compilar programas", "Diseñar interfaces"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué es una función en programación?",
                    "opciones": ["Un bloque de código reutilizable", "Un tipo de dato", "Un programa completo", "Una variable especial"],
                    "respuesta_correcta": 0
                },
                {
                    "pregunta": "¿Cuál es la diferencia entre '==' y '=' en programación?",
                    "opciones": ["No hay diferencia", "== compara, = asigna", "= compara, == asigna", "Ambos asignan valores"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué es una base de datos?",
                    "opciones": ["Un programa de juegos", "Sistema para almacenar y organizar información", "Un tipo de virus", "Un navegador web"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué significa 'CSS'?",
                    "opciones": ["Cascading Style Sheets", "Computer Style System", "Creative Style Software", "Central Security System"],
                    "respuesta_correcta": 0
                },
                {
                    "pregunta": "¿Qué es Git?",
                    "opciones": ["Un lenguaje de programación", "Un sistema de control de versiones", "Un navegador web", "Una base de datos"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Cuál es un entorno de desarrollo integrado (IDE)?",
                    "opciones": ["Visual Studio Code", "Google Chrome", "Microsoft Word", "Spotify"],
                    "respuesta_correcta": 0
                }
            ],
            "Redes": [
                {
                    "pregunta": "¿Qué significa 'TCP/IP'?",
                    "opciones": ["Transmission Control Protocol/Internet Protocol", "Total Computer Protocol", "Technical Communication Protocol", "Transfer Control Program"],
                    "respuesta_correcta": 0
                },
                {
                    "pregunta": "¿Cuál es la función de un router?",
                    "opciones": ["Almacenar datos", "Dirigir tráfico de red", "Ejecutar programas", "Mostrar imágenes"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué es una dirección IP?",
                    "opciones": ["Identificador único en una red", "Un tipo de cable", "Un programa", "Un virus"],
                    "respuesta_correcta": 0
                },
                {
                    "pregunta": "¿Qué significa 'LAN'?",
                    "opciones": ["Local Area Network", "Large Area Network", "Limited Access Network", "Linear Application Network"],
                    "respuesta_correcta": 0
                },
                {
                    "pregunta": "¿Cuál es el puerto estándar para HTTP?",
                    "opciones": ["21", "25", "80", "443"],
                    "respuesta_correcta": 2
                },
                {
                    "pregunta": "¿Qué significa 'DNS'?",
                    "opciones": ["Domain Name System", "Data Network Service", "Digital Network Security", "Direct Network Stream"],
                    "respuesta_correcta": 0
                },
                {
                    "pregunta": "¿Cuál es el puerto estándar para HTTPS?",
                    "opciones": ["80", "21", "443", "25"],
                    "respuesta_correcta": 2
                },
                {
                    "pregunta": "¿Qué es un switch de red?",
                    "opciones": ["Un cable de red", "Dispositivo que conecta múltiples dispositivos en una LAN", "Un tipo de router", "Un protocolo de red"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué significa 'WAN'?",
                    "opciones": ["Wide Area Network", "Wireless Access Network", "Web Application Network", "Windows Area Network"],
                    "respuesta_correcta": 0
                },
                {
                    "pregunta": "¿Cuál es la función de un modem?",
                    "opciones": ["Amplificar señales", "Modular y demodular señales digitales", "Guardar archivos", "Ejecutar programas"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué es el protocolo FTP?",
                    "opciones": ["File Transfer Protocol", "Fast Time Protocol", "Flexible Text Protocol", "Final Transfer Program"],
                    "respuesta_correcta": 0
                },
                {
                    "pregunta": "¿Qué significa 'MAC Address'?",
                    "opciones": ["Dirección física única de una tarjeta de red", "Tipo de computadora Apple", "Protocolo de seguridad", "Sistema operativo"],
                    "respuesta_correcta": 0
                },
                {
                    "pregunta": "¿Qué es una VPN?",
                    "opciones": ["Very Private Network", "Virtual Private Network", "Verified Personal Network", "Variable Protocol Network"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Cuál es el propósito de una máscara de subred?",
                    "opciones": ["Ocultar la red", "Definir qué parte de la IP es de red y cuál de host", "Acelerar la conexión", "Comprimir datos"],
                    "respuesta_correcta": 1
                },
                {
                    "pregunta": "¿Qué protocolo usa el correo electrónico para envío?",
                    "opciones": ["HTTP", "FTP", "SMTP", "DNS"],
                    "respuesta_correcta": 2
                }
            ]
        }
        
        self.crear_pantalla_inicio()
    
    def centrar_ventana(self):
        """Centrar la ventana en la pantalla"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def cargar_iconos(self):
        """Cargar los iconos de las categorías"""
        try:
            for categoria, path in self.iconos_path.items():
                if os.path.exists(path):
                    # Cargar y redimensionar imagen
                    imagen = Image.open(path)
                    imagen = imagen.resize((50, 50), Image.Resampling.LANCZOS)
                    photo = ImageTk.PhotoImage(imagen)
                    self.iconos[categoria] = photo
                    self.iconos_refs.append(photo)  # Mantener referencia para evitar garbage collection
                else:
                    print(f"❌ No se encontró el icono para {categoria} en {path}")
                    self.iconos[categoria] = None
        except Exception as e:
            print(f"🚨 Error cargando iconos: {e}")
            # Si hay error, usar iconos vacíos
            for categoria in self.iconos_path.keys():
                self.iconos[categoria] = None
    
    def crear_ruleta_categorias(self, parent):
        """Crear una ruleta visual de categorías similar al Preguntados original"""
        ruleta_frame = tk.Frame(parent, bg=self.colores["fondo_principal"])
        ruleta_frame.pack(pady=15)
        
        # Canvas para dibujar la ruleta (reducido de 200x200 a 160x160)
        canvas = Canvas(ruleta_frame, width=160, height=160, 
                       bg=self.colores["fondo_principal"], highlightthickness=0)
        canvas.pack()
        
        # Categorías y sus colores
        categorias = ["IA", "Ciberseguridad", "Programacion", "Redes"]
        colores_ruleta = [self.colores[cat] for cat in categorias]
        
        # Dibujar sectores de la ruleta (radio reducido)
        centro_x, centro_y = 80, 80
        radio = 65
        
        for i, (categoria, color) in enumerate(zip(categorias, colores_ruleta)):
            # Calcular ángulos para cada sector (90 grados cada uno)
            start_angle = i * 90
            extent_angle = 90
            
            # Dibujar sector
            canvas.create_arc(centro_x - radio, centro_y - radio,
                            centro_x + radio, centro_y + radio,
                            start=start_angle, extent=extent_angle,
                            fill=color, outline="white", width=3)
            
            # Calcular posición para el texto/icono (convertir grados a radianes correctamente)
            # Tkinter usa grados en sentido horario desde las 3 en punto
            angle_medio = start_angle + 45  # Punto medio del sector
            angle_rad = math.radians(-angle_medio + 90)  # Ajustar para coordenadas correctas
            text_x = centro_x + (radio * 0.6) * math.cos(angle_rad)
            text_y = centro_y - (radio * 0.6) * math.sin(angle_rad)  # Invertir Y
            
            # Iconos de categorías
            iconos_texto = {"IA": "🤖", "Ciberseguridad": "🔒", 
                           "Programacion": "💻", "Redes": "🌐"}
            
            canvas.create_text(text_x, text_y, text=iconos_texto[categoria], 
                             font=("Arial", 20), fill="white")
        
        # Círculo central
        canvas.create_oval(centro_x - 15, centro_y - 15,
                          centro_x + 15, centro_y + 15,
                          fill=self.colores["fondo_secundario"], 
                          outline="white", width=2)
    
    def crear_pantalla_inicio(self):
        """Crear la pantalla de inicio del juego"""
        # Limpiar ventana
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Frame principal con gradiente simulado
        frame_principal = tk.Frame(self.root, bg=self.colores["fondo_principal"])
        frame_principal.pack(expand=True, fill="both", padx=15, pady=15)
        
        # Header con título principal
        header_frame = tk.Frame(frame_principal, bg=self.colores["fondo_secundario"], relief="ridge", bd=3)
        header_frame.pack(fill="x", pady=(0, 20))
        
        # Título principal con estilo más llamativo
        titulo = tk.Label(header_frame, text="🎯 PREGUNTADOS", 
                         font=("Arial Black", 28, "bold"), 
                         fg=self.colores["texto_secundario"], 
                         bg=self.colores["fondo_secundario"])
        titulo.pack(pady=10)
        
        # Subtítulo
        subtitulo = tk.Label(header_frame, text="TRIVIA TECNOLÓGICA", 
                           font=("Arial", 14, "bold"), 
                           fg=self.colores["azul_claro"], 
                           bg=self.colores["fondo_secundario"])
        subtitulo.pack(pady=(0, 10))
        
        # Frame central para contenido
        contenido_frame = tk.Frame(frame_principal, bg=self.colores["fondo_principal"])
        contenido_frame.pack(expand=True, fill="both")
        
        # Crear ruleta de categorías
        self.crear_ruleta_categorias(contenido_frame)
        
        # Frame para información de categorías
        info_frame = tk.Frame(contenido_frame, bg=self.colores["fondo_tarjeta"], relief="ridge", bd=2)
        info_frame.pack(fill="x", pady=15, padx=30)
        
        # Título de categorías
        tk.Label(info_frame, text="🎮 CATEGORÍAS DE JUEGO", 
                font=("Arial", 12, "bold"), 
                fg=self.colores["amarillo_insignia"], 
                bg=self.colores["fondo_tarjeta"]).pack(pady=8)
        
        # Grid de categorías con colores
        categorias_grid = tk.Frame(info_frame, bg=self.colores["fondo_tarjeta"])
        categorias_grid.pack(pady=8)
        
        categorias_info = [
            ("🤖 Inteligencia Artificial", self.colores["IA"]),
            ("🔒 Ciberseguridad", self.colores["Ciberseguridad"]),
            ("💻 Programación", self.colores["Programacion"]),
            ("🌐 Redes", self.colores["Redes"])
        ]
        
        for i, (texto, color) in enumerate(categorias_info):
            categoria_label = tk.Label(categorias_grid, text=texto, 
                                     font=("Arial", 10, "bold"), 
                                     fg="white", bg=color,
                                     padx=12, pady=6, relief="raised", bd=2)
            categoria_label.grid(row=i//2, column=i%2, padx=8, pady=4, sticky="ew")
        
        # Configurar columnas del grid
        categorias_grid.grid_columnconfigure(0, weight=1)
        categorias_grid.grid_columnconfigure(1, weight=1)
        
        # Instrucciones
        instrucciones = tk.Label(info_frame, 
                               text="¡Responde 3 preguntas correctas por categoría para ganar una insignia!", 
                               font=("Arial", 10, "italic"), 
                               fg=self.colores["verde_correcto"], 
                               bg=self.colores["fondo_tarjeta"])
        instrucciones.pack(pady=(8, 12))
        
        # Frame para botones de juego
        botones_frame = tk.Frame(contenido_frame, bg=self.colores["fondo_principal"])
        botones_frame.pack(pady=20)
        
        # Botón Single Player
        btn_single = tk.Button(botones_frame, text="🎮 MODO SINGLE PLAYER", 
                              font=("Arial", 12, "bold"),
                              bg=self.colores["boton_principal"], 
                              fg="white", 
                              padx=30, pady=12,
                              relief="raised", bd=3,
                              activebackground=self.colores["texto_secundario"],
                              command=lambda: self.iniciar_juego("single"))
        btn_single.pack(pady=8)
        
        # Botón Multiplayer
        btn_multi = tk.Button(botones_frame, text="👥 MODO MULTIPLAYER", 
                             font=("Arial", 12, "bold"),
                             bg=self.colores["azul_claro"], 
                             fg="white", 
                             padx=30, pady=12,
                             relief="raised", bd=3,
                             activebackground="#5a9fd1",
                             command=lambda: self.iniciar_juego("multiplayer"))
        btn_multi.pack(pady=8)
    
    def iniciar_juego(self, modo):
        """Inicializar el juego según el modo seleccionado"""
        self.modo_juego = modo
        self.jugador_actual = 1
        self.puntuacion_j1 = 0
        self.puntuacion_j2 = 0
        self.respuestas_correctas_j1 = {"IA": 0, "Ciberseguridad": 0, "Programacion": 0, "Redes": 0}
        self.respuestas_correctas_j2 = {"IA": 0, "Ciberseguridad": 0, "Programacion": 0, "Redes": 0}
        self.insignias_j1 = set()
        self.insignias_j2 = set()
        self.preguntas_usadas = set()
        
        self.crear_pantalla_juego()
    
    def crear_pantalla_juego(self):
        """Crear la interfaz principal del juego"""
        # Limpiar ventana
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Frame principal con nuevos colores
        self.frame_juego = tk.Frame(self.root, bg=self.colores["fondo_principal"])
        self.frame_juego.pack(expand=True, fill="both", padx=15, pady=15)
        
        # Header con información del juego
        self.crear_header()
        
        # Frame para la pregunta con diseño mejorado
        self.frame_pregunta = tk.Frame(self.frame_juego, bg=self.colores["fondo_tarjeta"], 
                                     relief="raised", bd=3)
        self.frame_pregunta.pack(fill="x", pady=15)
        
        # Frame para las opciones con nuevo estilo
        self.frame_opciones = tk.Frame(self.frame_juego, bg=self.colores["fondo_principal"])
        self.frame_opciones.pack(fill="x", pady=15)
        
        # Frame para botones de control
        self.frame_controles = tk.Frame(self.frame_juego, bg=self.colores["fondo_principal"])
        self.frame_controles.pack(fill="x", pady=15)
        
        # Seleccionar primera pregunta
        self.seleccionar_nueva_pregunta()
    
    def crear_header(self):
        """Crear el header con información del juego"""
        header = tk.Frame(self.frame_juego, bg=self.colores["fondo_secundario"], 
                         relief="raised", bd=3)
        header.pack(fill="x", pady=(0, 20))
        
        # Info del jugador actual y puntuación
        if self.modo_juego == "single":
            self.label_jugador = tk.Label(header, text="🎮 SINGLE PLAYER", 
                                        font=("Arial", 16, "bold"), 
                                        fg=self.colores["texto_secundario"], 
                                        bg=self.colores["fondo_secundario"])
            self.label_puntuacion = tk.Label(header, text=f"💎 Puntuación: {self.puntuacion_j1}", 
                                          font=("Arial", 14, "bold"), 
                                          fg=self.colores["amarillo_insignia"], 
                                          bg=self.colores["fondo_secundario"])
        else:
            self.label_jugador = tk.Label(header, text=f"👤 TURNO: JUGADOR {self.jugador_actual}", 
                                        font=("Arial", 16, "bold"), 
                                        fg=self.colores["texto_secundario"], 
                                        bg=self.colores["fondo_secundario"])
            self.label_puntuacion = tk.Label(header, text=f"J1: {self.puntuacion_j1} 💎 | J2: {self.puntuacion_j2} 💎", 
                                          font=("Arial", 14, "bold"), 
                                          fg=self.colores["amarillo_insignia"], 
                                          bg=self.colores["fondo_secundario"])
        
        self.label_jugador.pack(pady=8)
        self.label_puntuacion.pack(pady=5)
        
        # Frame para insignias con iconos
        self.frame_insignias = tk.Frame(header, bg=self.colores["fondo_secundario"])
        self.frame_insignias.pack(pady=15)
        
        # Título de insignias
        self.label_titulo_insignias = tk.Label(self.frame_insignias, text="🏆 INSIGNIAS OBTENIDAS", 
                                             font=("Arial", 12, "bold"), 
                                             fg=self.colores["amarillo_insignia"], 
                                             bg=self.colores["fondo_secundario"])
        self.label_titulo_insignias.pack(pady=(0, 8))
        
        # Frame para iconos de insignias
        self.frame_iconos_insignias = tk.Frame(self.frame_insignias, bg=self.colores["fondo_secundario"])
        self.frame_iconos_insignias.pack()
        
        self.actualizar_insignias()
    
    def actualizar_insignias(self):
        """Actualizar la visualización de insignias con iconos"""
        # Limpiar frame de iconos
        for widget in self.frame_iconos_insignias.winfo_children():
            widget.destroy()
        
        if self.modo_juego == "single":
            # Crear frame para las insignias del jugador
            frame_j1 = tk.Frame(self.frame_iconos_insignias, bg="#434C5E")
            frame_j1.pack()
            
            # Mostrar iconos de insignias obtenidas
            insignias_mostradas = 0
            for categoria in ["IA", "Ciberseguridad", "Programacion", "Redes"]:
                if categoria in self.insignias_j1:
                    if self.iconos[categoria]:
                        icono_label = tk.Label(frame_j1, image=self.iconos[categoria], bg="#434C5E")
                        icono_label.pack(side="left", padx=8)
                        # Agregar tooltip con nombre de categoría
                        self.crear_tooltip(icono_label, categoria)
                        insignias_mostradas += 1
                    else:
                        print(f"❌ No hay icono disponible para {categoria}")
            
            # Si no hay insignias, mostrar mensaje
            if insignias_mostradas == 0:
                tk.Label(frame_j1, text="Sin insignias obtenidas", 
                        font=("Arial", 10), fg="#D8DEE9", bg="#434C5E").pack()
                        
        else:
            # Modo multiplayer - mostrar insignias de ambos jugadores
            # Jugador 1
            tk.Label(self.frame_iconos_insignias, text="Jugador 1:", 
                    font=("Arial", 9, "bold"), fg="#81A1C1", bg="#434C5E").pack()
            frame_j1 = tk.Frame(self.frame_iconos_insignias, bg="#434C5E")
            frame_j1.pack(pady=2)
            
            insignias_j1 = 0
            for categoria in ["IA", "Ciberseguridad", "Programacion", "Redes"]:
                if categoria in self.insignias_j1:
                    if self.iconos[categoria]:
                        icono_label = tk.Label(frame_j1, image=self.iconos[categoria], bg="#434C5E")
                        icono_label.pack(side="left", padx=3)
                        self.crear_tooltip(icono_label, categoria)
                        insignias_j1 += 1
            
            if insignias_j1 == 0:
                tk.Label(frame_j1, text="Sin insignias", 
                        font=("Arial", 8), fg="#D8DEE9", bg="#434C5E").pack()
            
            # Jugador 2
            tk.Label(self.frame_iconos_insignias, text="Jugador 2:", 
                    font=("Arial", 9, "bold"), fg="#BF616A", bg="#434C5E").pack(pady=(5,0))
            frame_j2 = tk.Frame(self.frame_iconos_insignias, bg="#434C5E")
            frame_j2.pack(pady=2)
            
            insignias_j2 = 0
            for categoria in ["IA", "Ciberseguridad", "Programacion", "Redes"]:
                if categoria in self.insignias_j2:
                    if self.iconos[categoria]:
                        icono_label = tk.Label(frame_j2, image=self.iconos[categoria], bg="#434C5E")
                        icono_label.pack(side="left", padx=3)
                        self.crear_tooltip(icono_label, categoria)
                        insignias_j2 += 1
            
            if insignias_j2 == 0:
                tk.Label(frame_j2, text="Sin insignias", 
                        font=("Arial", 8), fg="#D8DEE9", bg="#434C5E").pack()
    
    def crear_tooltip(self, widget, texto):
        """Crear tooltip para mostrar nombre de categoría al pasar el mouse"""
        def mostrar_tooltip(event):
            tooltip = tk.Toplevel()
            tooltip.wm_overrideredirect(True)
            tooltip.configure(bg="#2E3440")
            
            label = tk.Label(tooltip, text=texto, font=("Arial", 9), 
                           fg="#ECEFF4", bg="#2E3440", padx=5, pady=2)
            label.pack()
            
            # Posicionar tooltip cerca del mouse
            x = widget.winfo_rootx() + 25
            y = widget.winfo_rooty() + 25
            tooltip.geometry(f"+{x}+{y}")
            
            # Destruir tooltip después de 2 segundos
            tooltip.after(2000, tooltip.destroy)
        
        widget.bind("<Enter>", mostrar_tooltip)
    
    def seleccionar_nueva_pregunta(self):
        """Seleccionar una nueva pregunta aleatoria"""
        # Obtener categorías disponibles excluyendo aquellas donde el jugador actual ya tiene insignia
        categorias_disponibles = list(self.preguntas.keys())
        
        # Filtrar categorías donde el jugador actual ya tiene insignia
        if self.jugador_actual == 1:
            categorias_disponibles = [cat for cat in categorias_disponibles if cat not in self.insignias_j1]
        else:
            categorias_disponibles = [cat for cat in categorias_disponibles if cat not in self.insignias_j2]
        
        # Si no hay categorías disponibles para este jugador, usar todas las categorías
        if not categorias_disponibles:
            categorias_disponibles = list(self.preguntas.keys())
        
        self.categoria_actual = random.choice(categorias_disponibles)
        
        # Obtener pregunta que no haya sido usada
        preguntas_categoria = self.preguntas[self.categoria_actual]
        preguntas_disponibles = []
        
        for i, pregunta in enumerate(preguntas_categoria):
            pregunta_id = f"{self.categoria_actual}_{i}"
            if pregunta_id not in self.preguntas_usadas:
                preguntas_disponibles.append((i, pregunta))
        
        # Si no hay preguntas disponibles en esta categoría, intentar con otra categoría
        if not preguntas_disponibles:
            # Buscar categoría con preguntas disponibles
            categoria_encontrada = None
            for cat in categorias_disponibles:
                for i in range(len(self.preguntas[cat])):
                    if f"{cat}_{i}" not in self.preguntas_usadas:
                        categoria_encontrada = cat
                        break
                if categoria_encontrada:
                    break
            
            # Si encontramos una categoría con preguntas disponibles, usarla
            if categoria_encontrada:
                self.categoria_actual = categoria_encontrada
                preguntas_categoria = self.preguntas[self.categoria_actual]
                preguntas_disponibles = []
                
                for i, pregunta in enumerate(preguntas_categoria):
                    pregunta_id = f"{self.categoria_actual}_{i}"
                    if pregunta_id not in self.preguntas_usadas:
                        preguntas_disponibles.append((i, pregunta))
            else:
                # No hay preguntas disponibles en las categorías filtradas, 
                # verificar si hay preguntas en todas las categorías
                todas_las_categorias = list(self.preguntas.keys())
                categoria_con_preguntas = None
                
                for cat in todas_las_categorias:
                    for i in range(len(self.preguntas[cat])):
                        if f"{cat}_{i}" not in self.preguntas_usadas:
                            categoria_con_preguntas = cat
                            break
                    if categoria_con_preguntas:
                        break
                
                if categoria_con_preguntas:
                    # Usar cualquier categoría disponible
                    self.categoria_actual = categoria_con_preguntas
                    preguntas_categoria = self.preguntas[self.categoria_actual]
                    preguntas_disponibles = []
                    
                    for i, pregunta in enumerate(preguntas_categoria):
                        pregunta_id = f"{self.categoria_actual}_{i}"
                        if pregunta_id not in self.preguntas_usadas:
                            preguntas_disponibles.append((i, pregunta))
                else:
                    # No hay más preguntas disponibles, terminar juego
                    self.terminar_juego()
                    return
        
        # Seleccionar pregunta aleatoria
        indice, self.pregunta_actual = random.choice(preguntas_disponibles)
        pregunta_id = f"{self.categoria_actual}_{indice}"
        self.preguntas_usadas.add(pregunta_id)
        
        self.mostrar_pregunta()
    
    def mostrar_pregunta(self):
        """Mostrar la pregunta actual en la interfaz"""
        # Actualizar header primero
        self.actualizar_header()
        
        # Limpiar frames
        for widget in self.frame_pregunta.winfo_children():
            widget.destroy()
        for widget in self.frame_opciones.winfo_children():
            widget.destroy()
        for widget in self.frame_controles.winfo_children():
            widget.destroy()
        
        # Mostrar categoría con color específico
        color_categoria = self.colores[self.categoria_actual]
        categoria_frame = tk.Frame(self.frame_pregunta, bg=color_categoria, relief="raised", bd=2)
        categoria_frame.pack(fill="x", pady=(10, 0))
        
        categoria_label = tk.Label(categoria_frame, text=f"📂 {self.categoria_actual.upper()}", 
                                 font=("Arial", 14, "bold"), 
                                 fg="white", bg=color_categoria)
        categoria_label.pack(pady=8)
        
        # Mostrar pregunta
        pregunta_label = tk.Label(self.frame_pregunta, text=self.pregunta_actual["pregunta"], 
                                font=("Arial", 16, "bold"), 
                                fg=self.colores["texto_principal"], 
                                bg=self.colores["fondo_tarjeta"], 
                                wraplength=700, pady=20)
        pregunta_label.pack(pady=20, padx=20)
        
        # Mostrar opciones con nuevo sistema
        self.botones_opciones = []  # Guardar referencia a los botones
        
        for i, opcion in enumerate(self.pregunta_actual["opciones"]):
            # Frame para cada opción (más estrecho)
            opcion_frame = tk.Frame(self.frame_opciones, bg=self.colores["fondo_principal"])
            opcion_frame.pack(pady=6, padx=80)  # Más padding horizontal para hacer más estrecho
            
            # Botón estilizado para cada opción
            btn_opcion = tk.Button(opcion_frame, 
                                 text=f"{chr(65+i)}) {opcion}",
                                 font=("Arial", 12, "bold"),
                                 bg="white",  # Fondo blanco por defecto
                                 fg="black",  # Texto negro para contraste
                                 relief="solid", bd=2,
                                 padx=15, pady=10,
                                 width=50,  # Ancho fijo más pequeño
                                 activebackground="#f0f0f0",
                                 command=lambda idx=i: self.responder_directamente(idx))
            btn_opcion.pack()
            self.botones_opciones.append(btn_opcion)
        
        # Solo botón de menú (quitar botón de responder)
        controles_frame = tk.Frame(self.frame_controles, bg=self.colores["fondo_principal"])
        controles_frame.pack(expand=True, fill="x", pady=20)
        
        # Botón para volver al menú (centrado)
        btn_menu = tk.Button(controles_frame, text="🏠 MENÚ PRINCIPAL", 
                           font=("Arial", 14, "bold"),
                           bg=self.colores["rojo_incorrecto"], 
                           fg="white", 
                           padx=40, pady=15,
                           relief="raised", bd=3,
                           activebackground="#e55a4e",
                           command=self.crear_pantalla_inicio)
        btn_menu.pack(pady=10)
    
    def responder_directamente(self, indice_seleccionado):
        """Responder directamente al hacer clic en una opción"""
        respuesta_correcta = self.pregunta_actual["respuesta_correcta"]
        
        # Cambiar colores de todos los botones
        for i, btn in enumerate(self.botones_opciones):
            if i == respuesta_correcta:
                # Marcar la respuesta correcta en verde
                btn.config(bg=self.colores["verde_correcto"], fg="white")
            elif i == indice_seleccionado and i != respuesta_correcta:
                # Marcar la respuesta seleccionada incorrecta en rojo
                btn.config(bg=self.colores["rojo_incorrecto"], fg="white")
            else:
                # Dejar las demás opciones en gris claro
                btn.config(bg="#e0e0e0", fg="black")
            
            # Deshabilitar todos los botones
            btn.config(state="disabled")
        
        # Determinar jugador actual
        if self.modo_juego == "single":
            jugador_actual = 1
        else:
            jugador_actual = self.jugador_actual
        
        # Verificar si la respuesta es correcta
        if indice_seleccionado == respuesta_correcta:
            # Respuesta correcta
            if jugador_actual == 1:
                self.puntuacion_j1 += 10
                self.respuestas_correctas_j1[self.categoria_actual] += 1
                # Verificar insignia (ahora requiere 3 respuestas correctas)
                if self.respuestas_correctas_j1[self.categoria_actual] >= 3:
                    self.insignias_j1.add(self.categoria_actual)
                    messagebox.showinfo("🏆 ¡INSIGNIA OBTENIDA!", 
                                      f"¡Felicidades! Has obtenido la insignia de {self.categoria_actual}!")
            else:
                self.puntuacion_j2 += 10
                self.respuestas_correctas_j2[self.categoria_actual] += 1
                # Verificar insignia (ahora requiere 3 respuestas correctas)
                if self.respuestas_correctas_j2[self.categoria_actual] >= 3:
                    self.insignias_j2.add(self.categoria_actual)
                    messagebox.showinfo("🏆 ¡INSIGNIA OBTENIDA!", 
                                      f"¡Felicidades Jugador 2! Has obtenido la insignia de {self.categoria_actual}!")
        
        # Cambiar turno en modo multiplayer
        if self.modo_juego == "multiplayer":
            self.jugador_actual = 2 if self.jugador_actual == 1 else 1
        
        # Continuar después de 2 segundos
        self.root.after(2000, self.continuar_juego)
    
    def continuar_juego(self):
        """Continuar el juego después de mostrar el resultado"""
        # Verificar si el juego debe terminar
        if self.verificar_fin_juego():
            self.terminar_juego()
        else:
            # Actualizar la interfaz antes de continuar
            try:
                self.actualizar_header()
            except tk.TclError:
                # Los widgets ya no existen, el juego puede haber terminado
                return
            
            # Continuar con nueva pregunta
            self.seleccionar_nueva_pregunta()
    

    
    def actualizar_header(self):
        """Actualizar la información del header"""
        try:
            if self.modo_juego == "single":
                self.label_puntuacion.config(text=f"💎 Puntuación: {self.puntuacion_j1}")
            else:
                self.label_jugador.config(text=f"👤 TURNO: JUGADOR {self.jugador_actual}")
                self.label_puntuacion.config(text=f"J1: {self.puntuacion_j1} 💎 | J2: {self.puntuacion_j2} 💎")
            
            self.actualizar_insignias()
        except tk.TclError:
            # Los widgets ya no existen, crear nueva pantalla
            self.crear_pantalla_juego()
    
    def verificar_fin_juego(self):
        """Verificar si el juego debe terminar"""
        if self.modo_juego == "single":
            # En single player, el juego termina cuando se obtienen todas las insignias
            return len(self.insignias_j1) == 4
        else:
            # En multiplayer, el juego termina cuando un jugador obtiene todas las insignias
            return len(self.insignias_j1) == 4 or len(self.insignias_j2) == 4
    
    def terminar_juego(self):
        """Mostrar la pantalla de resultados finales"""
        # Limpiar ventana
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Frame principal con nuevo estilo
        frame_resultados = tk.Frame(self.root, bg=self.colores["fondo_principal"])
        frame_resultados.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Título
        titulo = tk.Label(frame_resultados, text="🎊 ¡JUEGO TERMINADO! 🎊", 
                         font=("Arial", 32, "bold"), 
                         fg=self.colores["verde_correcto"], 
                         bg=self.colores["fondo_principal"])
        titulo.pack(pady=(0, 30))
        
        # Resultados
        if self.modo_juego == "single":
            resultado_texto = f"""🎮 Modo Single Player

🏆 Puntuación Final: {self.puntuacion_j1} puntos

🥇 Insignias Obtenidas: {len(self.insignias_j1)}/4

{'¡Felicidades! ¡Has obtenido todas las insignias!' if len(self.insignias_j1) == 4 else '¡Sigue practicando para obtener todas las insignias!'}"""
            
            resultado_label = tk.Label(frame_resultados, text=resultado_texto, font=("Arial", 12), 
                                     fg="#ECEFF4", bg="#2E3440", justify="center")
            resultado_label.pack(pady=(0, 20))
            
            # Mostrar iconos de insignias obtenidas
            if self.insignias_j1:
                insignias_frame = tk.Frame(frame_resultados, bg="#2E3440")
                insignias_frame.pack(pady=20)
                
                tk.Label(insignias_frame, text="🏆 Insignias Obtenidas:", 
                        font=("Arial", 14, "bold"), fg="#EBCB8B", bg="#2E3440").pack(pady=(0, 10))
                
                iconos_frame = tk.Frame(insignias_frame, bg="#2E3440")
                iconos_frame.pack()
                
                for categoria in ["IA", "Ciberseguridad", "Programacion", "Redes"]:
                    if categoria in self.insignias_j1 and self.iconos[categoria]:
                        # Frame para cada insignia
                        insignia_container = tk.Frame(iconos_frame, bg="#434C5E", relief="ridge", bd=2)
                        insignia_container.pack(side="left", padx=10, pady=5)
                        
                        # Icono
                        icono_label = tk.Label(insignia_container, image=self.iconos[categoria], bg="#434C5E")
                        icono_label.pack(pady=5)
                        
                        # Nombre de categoría
                        tk.Label(insignia_container, text=categoria, font=("Arial", 10, "bold"), 
                               fg="#ECEFF4", bg="#434C5E").pack(pady=(0, 5))
            
        else:
            # Determinar ganador
            if len(self.insignias_j1) == 4:
                ganador = "Jugador 1"
            elif len(self.insignias_j2) == 4:
                ganador = "Jugador 2"
            else:
                if self.puntuacion_j1 > self.puntuacion_j2:
                    ganador = "Jugador 1"
                elif self.puntuacion_j2 > self.puntuacion_j1:
                    ganador = "Jugador 2"
                else:
                    ganador = "¡Empate!"
            
            resultado_texto = f"""👥 Modo Multiplayer

🏆 Ganador: {ganador}

📊 Resultados:
Jugador 1: {self.puntuacion_j1} puntos - {len(self.insignias_j1)} insignias
Jugador 2: {self.puntuacion_j2} puntos - {len(self.insignias_j2)} insignias"""
            
            resultado_label = tk.Label(frame_resultados, text=resultado_texto, font=("Arial", 12), 
                                     fg="#ECEFF4", bg="#2E3440", justify="center")
            resultado_label.pack(pady=(0, 20))
            
            # Mostrar insignias de ambos jugadores
            insignias_frame = tk.Frame(frame_resultados, bg="#2E3440")
            insignias_frame.pack(pady=20)
            
            # Jugador 1
            j1_frame = tk.Frame(insignias_frame, bg="#2E3440")
            j1_frame.pack(side="left", padx=20)
            
            tk.Label(j1_frame, text="🥇 Jugador 1", font=("Arial", 14, "bold"), 
                   fg="#81A1C1", bg="#2E3440").pack(pady=(0, 10))
            
            j1_iconos = tk.Frame(j1_frame, bg="#2E3440")
            j1_iconos.pack()
            
            for categoria in ["IA", "Ciberseguridad", "Programacion", "Redes"]:
                if categoria in self.insignias_j1 and self.iconos[categoria]:
                    insignia_container = tk.Frame(j1_iconos, bg="#434C5E", relief="ridge", bd=2)
                    insignia_container.pack(side="left", padx=5, pady=5)
                    
                    icono_label = tk.Label(insignia_container, image=self.iconos[categoria], bg="#434C5E")
                    icono_label.pack(pady=3)
                    
                    tk.Label(insignia_container, text=categoria, font=("Arial", 8), 
                           fg="#ECEFF4", bg="#434C5E").pack(pady=(0, 3))
            
            if not self.insignias_j1:
                tk.Label(j1_iconos, text="Sin insignias", font=("Arial", 10), 
                       fg="#D8DEE9", bg="#2E3440").pack()
            
            # Jugador 2
            j2_frame = tk.Frame(insignias_frame, bg="#2E3440")
            j2_frame.pack(side="left", padx=20)
            
            tk.Label(j2_frame, text="🥈 Jugador 2", font=("Arial", 14, "bold"), 
                   fg="#BF616A", bg="#2E3440").pack(pady=(0, 10))
            
            j2_iconos = tk.Frame(j2_frame, bg="#2E3440")
            j2_iconos.pack()
            
            for categoria in ["IA", "Ciberseguridad", "Programacion", "Redes"]:
                if categoria in self.insignias_j2 and self.iconos[categoria]:
                    insignia_container = tk.Frame(j2_iconos, bg="#434C5E", relief="ridge", bd=2)
                    insignia_container.pack(side="left", padx=5, pady=5)
                    
                    icono_label = tk.Label(insignia_container, image=self.iconos[categoria], bg="#434C5E")
                    icono_label.pack(pady=3)
                    
                    tk.Label(insignia_container, text=categoria, font=("Arial", 8), 
                           fg="#ECEFF4", bg="#434C5E").pack(pady=(0, 3))
            
            if not self.insignias_j2:
                tk.Label(j2_iconos, text="Sin insignias", font=("Arial", 10), 
                       fg="#D8DEE9", bg="#2E3440").pack()
        
        # Botones
        botones_frame = tk.Frame(frame_resultados, bg="#2E3440")
        botones_frame.pack(pady=30)
        
        # Botones con nuevo estilo
        tk.Button(botones_frame, text="🔄 JUGAR NUEVAMENTE", font=("Arial", 16, "bold"),
                 bg=self.colores["boton_principal"], fg="white", 
                 padx=40, pady=15, relief="raised", bd=3,
                 activebackground=self.colores["texto_secundario"],
                 command=self.crear_pantalla_inicio).pack(pady=10)
        
        tk.Button(botones_frame, text="❌ SALIR", font=("Arial", 16, "bold"),
                 bg=self.colores["rojo_incorrecto"], fg="white", 
                 padx=40, pady=15, relief="raised", bd=3,
                 activebackground="#e55a4e",
                 command=self.root.quit).pack(pady=10)
    
    def ejecutar(self):
        """Ejecutar la aplicación"""
        self.root.mainloop()

# Ejecutar el juego
if __name__ == "__main__":
    juego = PreguntadosGame()
    juego.ejecutar()
