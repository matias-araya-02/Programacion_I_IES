# Agenda de Contactos - Sistema CRUD

## Descripción
Esta es una aplicación de agenda de contactos desarrollada en Python con Tkinter que implementa un sistema CRUD completo (Crear, Leer, Actualizar, Eliminar) con eliminación lógica.

## Características principales

### ✅ CRUD Completo
- **Crear**: Añadir nuevos contactos
- **Leer**: Visualizar todos los contactos
- **Actualizar**: Editar contactos existentes
- **Eliminar**: Eliminación lógica (baja lógica)

### ✅ Eliminación Lógica
- Los contactos no se borran físicamente de la base de datos
- Se marcan como "eliminados" pero permanecen en el sistema
- Posibilidad de restaurar contactos eliminados
- Toggle para mostrar/ocultar contactos eliminados

### ✅ Interfaz Intuitiva
- Formulario simple para entrada de datos
- Botones con colores distintivos para cada acción
- Tabla (Treeview) para visualizar contactos
- Mensajes informativos para confirmaciones y errores

## Funcionalidades

### 1. Añadir Contacto
- Llenar los campos "Nombre" y "Teléfono"
- Hacer clic en el botón **AÑADIR** (verde)
- Validación de campos obligatorios

### 2. Editar Contacto
- **Opción 1**: Seleccionar un contacto y hacer clic en **EDITAR** (naranja)
- **Opción 2**: Hacer doble clic sobre el contacto en la tabla
- Los campos se llenan automáticamente con los datos del contacto
- El botón **AÑADIR** cambia a **ACTUALIZAR** (morado)
- Solo se pueden editar contactos activos

### 3. Eliminar Contacto (Baja Lógica)
- Seleccionar un contacto de la tabla
- Hacer clic en **ELIMINAR** (rojo)
- Confirmar la eliminación en el cuadro de diálogo
- El contacto se marca como "Eliminado" pero no se borra

### 4. Mostrar/Ocultar Contactos Eliminados
- Usar el checkbox "Mostrar contactos eliminados"
- **Sin marcar**: Solo muestra contactos activos
- **Marcado**: Muestra todos los contactos (activos y eliminados)

### 5. Restaurar Contacto
- Marcar el checkbox para mostrar contactos eliminados
- Seleccionar un contacto con estado "Eliminado"
- Hacer clic en **RESTAURAR** (azul)
- El contacto vuelve a estar activo

### 6. Cancelar Edición
- Durante la edición, hacer clic en **CANCELAR** (gris)
- Limpia los campos y vuelve al modo de añadir

## Estados de los Contactos
- **Activo**: Contacto disponible y visible por defecto
- **Eliminado**: Contacto marcado como eliminado (baja lógica)

## Estructura de Datos
Cada contacto se almacena como una lista con:
```python
[id, nombre, teléfono, activo]
# activo: True = Activo, False = Eliminado
```

## Colores de los Botones
- 🟢 **Verde**: AÑADIR / ACTUALIZAR
- 🟠 **Naranja**: EDITAR
- 🔴 **Rojo**: ELIMINAR
- 🔵 **Azul**: RESTAURAR
- ⚫ **Gris**: CANCELAR
- 🟣 **Morado**: ACTUALIZAR (durante edición)

## Validaciones
- Campos obligatorios (nombre y teléfono)
- No se pueden editar contactos eliminados
- Confirmación antes de eliminar
- Mensajes informativos para todas las acciones

## Ejecución
```bash
python agenda_tkinter.py
```

## Requisitos
- Python 3.x
- Tkinter (incluido por defecto en Python)

---
*Desarrollado como sistema CRUD completo con eliminación lógica para gestión de contactos*