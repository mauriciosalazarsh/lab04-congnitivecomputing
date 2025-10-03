from werkzeug.security import generate_password_hash
import mysql.connector

def create_admin_user():
    password_hash = generate_password_hash('admin123')
    
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='lab04_flask'
        )
        
        cursor = connection.cursor()
        cursor.execute("DELETE FROM admin_users WHERE username = 'admin'")
        cursor.execute("INSERT INTO admin_users (username, password) VALUES (%s, %s)", 
                      ('admin', password_hash))
        
        connection.commit()
        print("Usuario administrador creado exitosamente")
        print("Username: admin")
        print("Password: admin123")
        
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()

if __name__ == '__main__':
    create_admin_user()