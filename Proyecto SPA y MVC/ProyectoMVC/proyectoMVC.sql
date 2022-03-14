CREATE DATABASE proyectoMVC;
USE proyectoMVC;


CREATE TABLE persona (
	id_persona INT,
	nombres VARCHAR(25),
	apellidos VARCHAR(25),
	documento VARCHAR(20),
	id_tipo_documento INT,
	fecha_nacimiento DATE,
	lugar_residencia INT,
	email VARCHAR(100),
	telefono BIGINT,
	usuario VARCHAR(10),
	contraseña VARCHAR(20),
	PRIMARY KEY(id_persona)
);
