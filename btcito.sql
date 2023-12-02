--CREATE TABLE control_asistencia(id INTEGER PRIMARY KEY AUTOINCREMENT, 
--responsable TEXT,
--emoji_seleccionado TEXT,
--momento_toma_asistencia TIMESTAMP,
--semana_de_asistencia INTEGER, 
--bloque_de_asistencia TEXT,
--FOREIGN KEY (semana_de_asistencia) REFERENCES semanas(id),  
--FOREIGN KEY (responsable) REFERENCES usuarios(codigo_usuario));

--SELECT * FROM tareas;
-
--CREATE TABLE asistencia(id INTEGER PRIMARY KEY AUTOINCREMENT, 
--estado_asistencia TEXT,
--emoji_enviado TEXT,
--momento_envio TIMESTAMP,
--codigo_estudiante TEXT, 
--bloque TEXT,
--FOREIGN KEY (codigo_estudiante) REFERENCES usuarios(codigo_usuario));


--CREATE TABLE semanas(id INTEGER PRIMARY KEY AUTOINCREMENT, 
--tema TEXT,
--documentacion_extra TEXT,
--diapositivas TEXT,
--lectures TEXT, 
--fecha_inicio TIMESTAMP,
--fecha_finalizacion TIMESTAMP);


--DELETE FROM control_asistencia;
--INSERT INTO asistencia(estado_asistencia, emoji_enviado, momento_envio, codigo_estudiante)
--VALUES ('AUSENTE', 'frog', '2023-12-01 10:30:00', 'Y23C2-AMORENO');

--DELETE FROM usuarios WHERE codigo_usuario = "Y23C2-JPEREZ";
--SELECT *FROM asistencia;


--UPDATE sqlite_sequence SET seq = -1 WHERE name = 'semanas'; 
--Sirve para resetear el conteo del id de una tabla

-- Consultas para agregar todos los datos a la tabla SEMANAS

--INSERT INTO usuarios(codigo_usuario, nombre, apellido, grupo) VALUES ('Y23C1-CRUIZ', 'Carlos', 'Ruiz', 'STAFF');

--INSERT INTO semanas(tema, documentacion_extra, diapositivas, lectures, fecha_inicio, fecha_finalizacion) 
--VALUES('Scratch', 'https://acortar.link/7SLsLa', 'https://acortar.link/pbdgKB', 'https://acortar.link/b7UQjk', '2023-07-08', '2023-07-14');

--INSERT INTO semanas(tema, documentacion_extra, diapositivas, lectures, fecha_inicio, fecha_finalizacion) 
--VALUES('C', 'https://acortar.link/w3h69x', 'https://acortar.link/FtqsF3', 'https://acortar.link/ZsGNtr', '2023-07-15', '2023-07-21');

--INSERT INTO semanas(tema, documentacion_extra, diapositivas, lectures, fecha_inicio, fecha_finalizacion) 
--VALUES('Arrays', 'https://acortar.link/R0s74z', 'https://acortar.link/o8GViK', 'https://acortar.link/G2VWD9', '2023-07-22', '2023-07-28');

--INSERT INTO semanas(tema, documentacion_extra, diapositivas, lectures, fecha_inicio, fecha_finalizacion) 
--VALUES('Algoritmos', 'https://acortar.link/0srq9r', 'https://acortar.link/G0uIqx', 'https://acortar.link/dPhwQ7', '2023-07-29', '2023-08-04');

--INSERT INTO semanas(tema, documentacion_extra, diapositivas, lectures, fecha_inicio, fecha_finalizacion) 
--VALUES('Memoria', 'https://acortar.link/material_extra', 'https://acortar.link/diapo', 'https://acortar.link/lecture4', '2023-08-05', '2023-08-11');

--INSERT INTO semanas(tema, documentacion_extra, diapositivas, lectures, fecha_inicio, fecha_finalizacion) 
--VALUES('Estructuras de datos', 'https://acortar.link/docu_extra', 'https://acortar.link/diapo16-17', 'https://acortar.link/lecture5', '2023-08-12', '2023-08-18');

--INSERT INTO semanas(tema, documentacion_extra, diapositivas, lectures, fecha_inicio, fecha_finalizacion) 
--VALUES('Python', 'https://acortar.link/python_book', 'https://acortar.link/diapo19-20', 'https://acortar.link/lecture6', '2023-08-19', '2023-08-25');

--UPDATE semanas SET documentacion_extra = 'https://acortar.link/python_book' WHERE tema = 'Python';

--INSERT INTO semanas(tema, documentacion_extra, diapositivas, lectures, fecha_inicio, fecha_finalizacion) 
--VALUES('SQL', 'https://acortar.link/doc_sql', 'https://acortar.link/diapo23-24', 'https://acortar.link/lecture7', '2023-08-26', '2023-09-01');

--INSERT INTO semanas(tema, documentacion_extra, diapositivas, lectures, fecha_inicio, fecha_finalizacion) 
--VALUES('HTML, CSS, JavaScript', 'https://acortar.link/doc_html', 'https://acortar.link/diapo25-26', 'https://acortar.link/lecture8', '2023-09-02', '2023-09-08');

--INSERT INTO semanas(tema, documentacion_extra, diapositivas, lectures, fecha_inicio, fecha_finalizacion) 
--VALUES('Flask', 'https://acortar.link/doc_flask', 'https://acortar.link/diapo25-26', 'https://acortar.link/lecture9', '2023-09-09', '2023-09-15');


-- Consultas para agregar todo a la tabla TAREAS

--INSERT INTO tareas(tipo_asignacion, fecha_liberacion, fecha_limite, semana_correspondiente)
--VALUES('Pset 0', '2023-07-08', '2023-07-14', 1);

--INSERT INTO tareas(tipo_asignacion, fecha_liberacion, fecha_limite, semana_correspondiente)
--VALUES('Lab 1, Pset 1', '2023-07-15', '2023-07-21', 2);

--INSERT INTO tareas(tipo_asignacion, fecha_liberacion, fecha_limite, semana_correspondiente)
--VALUES('Lab 2, Pset 2', '2023-07-22', '2023-07-28', 3);

--INSERT INTO tareas(tipo_asignacion, fecha_liberacion, fecha_limite, semana_correspondiente)
--VALUES('Lab 3, Pset 3', '2023-07-29', '2023-08-04', 4);
--
--INSERT INTO tareas(tipo_asignacion, fecha_liberacion, fecha_limite, semana_correspondiente)
--VALUES('Lab 4, Pset 4', '2023-08-05', '2023-08-11', 5);

--INSERT INTO tareas(tipo_asignacion, fecha_liberacion, fecha_limite, semana_correspondiente)
--VALUES('Lab 5, Pset 5', '2023-08-12', '2023-08-18', 6);

--INSERT INTO tareas(tipo_asignacion, fecha_liberacion, fecha_limite, semana_correspondiente)
--VALUES('Lab 6, Pset 6', '2023-08-19', '2023-08-25', 7);

--INSERT INTO tareas(tipo_asignacion, fecha_liberacion, fecha_limite, semana_correspondiente)
--VALUES('Lab 7, Pset 7', '2023-08-26', '2023-09-01', 8);

--INSERT INTO tareas(tipo_asignacion, fecha_liberacion, fecha_limite, semana_correspondiente)
--VALUES('Lab 8, Pset 8', '2023-09-02', '2023-09-08', 9);

--INSERT INTO tareas(tipo_asignacion, fecha_liberacion, fecha_limite, semana_correspondiente)
--VALUES('Lab 9, Pset 9', '2023-09-09', '2023-09-15', 10);