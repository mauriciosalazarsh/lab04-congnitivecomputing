from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='lab04_flask'
    )
    return connection

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT id, username, password FROM admin_users WHERE username = %s", (username,))
            user = cursor.fetchone()
            
            if user and check_password_hash(user[2], password):
                session['user_id'] = user[0]
                session['username'] = user[1]
                flash('Login exitoso', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Usuario o contraseña incorrectos', 'error')
        except mysql.connector.Error as e:
            flash(f'Error de base de datos: {e}', 'error')
        finally:
            if connection:
                connection.close()
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Has cerrado sesión', 'info')
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, nombre, email, rol FROM usuarios ORDER BY id")
        users = cursor.fetchall()
    except mysql.connector.Error as e:
        flash(f'Error al cargar usuarios: {e}', 'error')
        users = []
    finally:
        if connection:
            connection.close()
    
    return render_template('dashboard.html', users=users)

@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        rol = request.form['rol']
        
        if not nombre or not email or not rol:
            flash('Todos los campos son obligatorios', 'error')
            return render_template('create_user.html')
        
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO usuarios (nombre, email, rol) VALUES (%s, %s, %s)", 
                         (nombre, email, rol))
            connection.commit()
            flash('Usuario creado exitosamente', 'success')
            return redirect(url_for('dashboard'))
        except mysql.connector.Error as e:
            flash(f'Error al crear usuario: {e}', 'error')
        finally:
            if connection:
                connection.close()
    
    return render_template('create_user.html')

@app.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        rol = request.form['rol']
        
        if not nombre or not email or not rol:
            flash('Todos los campos son obligatorios', 'error')
            return redirect(url_for('edit_user', user_id=user_id))
        
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute("UPDATE usuarios SET nombre = %s, email = %s, rol = %s WHERE id = %s", 
                         (nombre, email, rol, user_id))
            connection.commit()
            flash('Usuario actualizado exitosamente', 'success')
            return redirect(url_for('dashboard'))
        except mysql.connector.Error as e:
            flash(f'Error al actualizar usuario: {e}', 'error')
        finally:
            if connection:
                connection.close()
    
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, nombre, email, rol FROM usuarios WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        
        if not user:
            flash('Usuario no encontrado', 'error')
            return redirect(url_for('dashboard'))
    except mysql.connector.Error as e:
        flash(f'Error al cargar usuario: {e}', 'error')
        return redirect(url_for('dashboard'))
    finally:
        if connection:
            connection.close()
    
    return render_template('edit_user.html', user=user)

@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (user_id,))
        connection.commit()
        flash('Usuario eliminado exitosamente', 'success')
    except mysql.connector.Error as e:
        flash(f'Error al eliminar usuario: {e}', 'error')
    finally:
        if connection:
            connection.close()
    
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)