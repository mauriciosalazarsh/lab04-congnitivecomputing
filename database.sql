CREATE DATABASE IF NOT EXISTS lab04_flask;
USE lab04_flask;

CREATE TABLE IF NOT EXISTS admin_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    rol ENUM('admin', 'usuario') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO admin_users (username, password) VALUES 
('admin', 'pbkdf2:sha256:600000$salt$hash');

INSERT INTO usuarios (nombre, email, rol) VALUES 
('demo1', 'demo1@email.com', 'usuario'),
('demo2', 'demo2@email.com', 'admin'),
('demo3', 'demo3@email.com', 'usuario');