from PIL import Image
import os

# Verificar que los iconos existen y se pueden cargar
iconos_path = {
    "IA": "img/pngtree-ai-icon-png-image_15382528.png",
    "Ciberseguridad": "img/ciberseguridad.png", 
    "Programacion": "img/programacion.png",
    "Redes": "img/redes.png"
}

print("🔍 Verificando iconos de insignias...")
print("=" * 50)

for categoria, path in iconos_path.items():
    if os.path.exists(path):
        try:
            imagen = Image.open(path)
            print(f"✅ {categoria}: {path} - {imagen.size} pixels")
        except Exception as e:
            print(f"❌ {categoria}: Error al cargar {path} - {e}")
    else:
        print(f"❌ {categoria}: Archivo no encontrado - {path}")

print("=" * 50)
print("✨ Verificación completada!")