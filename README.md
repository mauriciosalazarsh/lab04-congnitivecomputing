# Lab04 

## Qué hace la aplicación

Es una app web donde un admin puede loguearse y gestionar usuarios (crear, ver, editar, eliminar). No hay registro público, solo el admin puede entrar.

## Archivos del proyecto

```
Lab04/
├── app.py                # La aplicación principal 
├── create_admin.py       # Para crear el usuario admin
├── database.sql          # Script de la base de datos
├── requirements.txt      # Las librerías que necesitas instalar
├── README.md            # Este archivo
└── templates/           # Los HTML
    ├── base.html        # Template base
    ├── login.html       # Página de login
    ├── dashboard.html   # Lista de usuarios
    ├── create_user.html # Crear usuario
    └── edit_user.html   # Editar usuario
```

## Cómo instalarlo para MacOS

### 1. Instalar MySQL
```bash
brew install mysql
brew services start mysql
```

### 2. Instalar las librerías de Python
```bash
pip install -r requirements.txt
```

### 3. Crear la base de datos
```bash
mysql -u root -p < database.sql
```

### 4. Crear el usuario admin
```bash
python3 create_admin.py
```

## Cómo ejecutarlo

```bash
python3 app.py
```

Después ve a: `http://localhost:5001`

**Login:**
- Usuario: `admin`
- Contraseña: `admin123`

## Funcionalidades

- **Login**: Solo el admin puede entrar, no hay registro
- **Ver usuarios**: Lista todos los usuarios en una tabla
- **Crear usuario**: Formulario para agregar nuevos usuarios
- **Editar usuario**: Modificar datos de usuarios existentes
- **Eliminar usuario**: Borrar usuarios (con confirmación)

## Base de datos

Usa MySQL con 2 tablas:

- `admin_users`: Para el login del admin
- `usuarios`: Los usuarios que se gestionan (nombre, email, rol)

## Tecnologías usadas

- Flask (Python)
- MySQL
- Bootstrap 5
- HTML/CSS

## Notas

- Las contraseñas se guardan hasheadas por seguridad
- La app corre en puerto 5001 para evitar conflictos
- Ya incluye usuarios de ejemplo: demo1, demo2, demo3

## Si algo no funciona

- Revisar que MySQL esté corriendo: `brew services start mysql`
- Si tiene contraseña en MySQL, cámbiela en `app.py` línea 13
- Si el puerto está ocupado, la app usa 5001 automáticamente
