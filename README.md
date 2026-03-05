# Galería de Arte - Proyecto Django

Sistema web de galería de arte desarrollado con Django que permite gestionar obras de arte, usuarios con diferentes roles (Administrador y Visualizador), y un sistema de contacto.

## 📋 Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Entorno virtual (recomendado)

## 🚀 Instalación

### 1. Clonar o descargar el proyecto

```bash
# Si usas Git
git clone <url-del-repositorio>

# O simplemente copia la carpeta del proyecto a tu PC
```

### 2. Crear y activar un entorno virtual

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**En Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias principales

Ejecuta los siguientes comandos para instalar todas las dependencias necesarias:

```bash
# Framework Django
pip install Django==4.2.7

# Django REST Framework para APIs
pip install djangorestframework==3.14.0
pip install djangorestframework-simplejwt==5.3.0

# Formularios con Bootstrap
pip install django-crispy-forms==2.4
pip install crispy-bootstrap5==2025.6
pip install django-bootstrap5==23.3

# CORS para APIs
pip install django-cors-headers==4.3.1

# Procesamiento de imágenes
pip install Pillow==10.1.0

### 4. Instalar todas las dependencias de una vez (Alternativa)

Si prefieres instalar todo de una vez, copia y pega este comando:

```bash
pip install Django==4.2.7 djangorestframework==3.14.0 djangorestframework-simplejwt==5.3.0 django-crispy-forms==2.4 crispy-bootstrap5==2025.6 django-bootstrap5==23.3 django-cors-headers==4.3.1 Pillow==10.1.0
```

## ⚙️ Configuración del Proyecto

### 1. Aplicar migraciones de la base de datos

```bash
python manage.py migrate
```

### 2. Crear un superusuario (Administrador)

```bash
python manage.py createsuperuser
```

Sigue las instrucciones en pantalla para crear tu usuario administrador.

### 3. Crear usuarios de prueba (Opcional)

El proyecto incluye un script para crear usuarios de prueba:

```bash
python crear_usuarios_prueba.py
```

Este script creará:
- **Administrador**: usuario: `admin_test`, contraseña: `admin123`
- **Visualizador**: usuario: `viewer_test`, contraseña: `viewer123`

## 🏃 Ejecutar el Proyecto

### Iniciar el servidor de desarrollo

```bash
python manage.py runserver
```

El proyecto estará disponible en: `http://127.0.0.1:8000/`

### Acceder al panel de administración

Visita: `http://127.0.0.1:8000/admin/`

## 📁 Estructura del Proyecto

```
AlbumEva3/
├── GaleriaDeArte/          # Configuración principal del proyecto
│   ├── settings.py         # Configuraciones
│   ├── urls.py            # URLs principales
│   └── wsgi.py            # Configuración WSGI
├── album/                  # App de gestión de obras de arte
├── usuarios/              # App de gestión de usuarios y autenticación
├── contacto/              # App de formulario de contacto
├── api_cliente/           # App de API REST
├── core/                  # App principal con templates base
├── media/                 # Archivos multimedia subidos
├── db.sqlite3            # Base de datos SQLite
└── manage.py             # Script de gestión de Django
```

## 🔑 Usuarios y Roles

El sistema cuenta con dos tipos de usuarios:

### Administrador
- Acceso completo al panel de administración
- Puede crear, editar y eliminar obras de arte
- Gestiona usuarios del sistema

### Visualizador
- Solo puede ver las obras de arte
- No tiene acceso al panel de administración

## 📧 Configuración de Email (Mailtrap)

El proyecto está configurado para usar Mailtrap para el envío de emails. Las credenciales están en `settings.py`:

```python
EMAIL_HOST = "sandbox.smtp.mailtrap.io"
EMAIL_PORT = 2525
EMAIL_HOST_USER = "868c8f97b52fe4"
EMAIL_HOST_PASSWORD = "d992688634fdea"
```

> **Nota**: Para producción, cambia estas credenciales por las de un servicio de email real.

## 🌍 Configuración Regional

El proyecto está configurado para:
- **Idioma**: Español (es-es)
- **Zona horaria**: America/Santiago

## 🛠️ Comandos Útiles

```bash
# Crear nuevas migraciones después de cambios en modelos
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Recopilar archivos estáticos
python manage.py collectstatic

# Crear superusuario
python manage.py createsuperuser

# Verificar usuarios existentes
python check_users.py
```

## 📝 Notas Importantes

1. **Base de datos**: El proyecto usa SQLite por defecto, ideal para desarrollo. Para producción, considera usar PostgreSQL o MySQL.

2. **SECRET_KEY**: La clave secreta en `settings.py` debe cambiarse en producción.

3. **DEBUG**: Asegúrate de establecer `DEBUG = False` en producción.

4. **ALLOWED_HOSTS**: Actualiza `ALLOWED_HOSTS` en `settings.py` con tu dominio en producción.

## 🐛 Solución de Problemas

### Error: "No module named 'django'"
```bash
# Asegúrate de tener el entorno virtual activado
pip install Django==4.2.7
```

### Error: "No such table"
```bash
# Ejecuta las migraciones
python manage.py migrate
```

### Error con Pillow en Windows
```bash
# Instala las herramientas de compilación de Visual C++ o usa:
pip install Pillow --only-binary :all:
```

## 📄 Licencia

Este proyecto es parte de una evaluación académica.

## 👥 Autores

- Moreno
- Alarcón
- Henríquez

---

**¿Necesitas ayuda?** Revisa la documentación oficial de Django: https://docs.djangoproject.com/
