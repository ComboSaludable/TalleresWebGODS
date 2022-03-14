from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL



app= Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST']= '127.0.0.1'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= '0812'
app.config['MYSQL_DB']= 'proyectoMVC'
mysql = MySQL(app)

#setting
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM persona')
    data = cur.fetchall()
    return render_template('index.html', contacts = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        id_persona = request.form['id_persona']
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        documento = request.form['documento']
        id_tipo_documento = request.form['id_tipo_documento']
        fecha_nacimiento = request.form['fecha_nacimiento']
        lugar_residencia = request.form['lugar_residencia']
        email = request.form['email']
        telefono = request.form['telefono']
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO persona VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (id_persona, nombres, apellidos, documento, id_tipo_documento, fecha_nacimiento, lugar_residencia, email, telefono, usuario, contraseña))
        mysql.connection.commit()
        flash('Contacto agregado satisfactoriamente')
        return redirect(url_for('index'))


@app.route('/edit/<string:id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM persona WHERE id_persona = %s', (id,))
    data = cur.fetchall()
    return render_template('edit-contact.html', contact = data[0])

@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        id_persona = request.form['id_persona']
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        documento = request.form['documento']
        id_tipo_documento = request.form['id_tipo_documento']
        fecha_nacimiento = request.form['fecha_nacimiento']
        lugar_residencia = request.form['lugar_residencia']
        email = request.form['email']
        telefono = request.form['telefono']
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
    cur = mysql.connection.cursor()
    cur.execute("""
    UPDATE persona
    SET id_persona = %s,
        nombres = %s,
        apellidos = %s,
        documento = %s,
        id_tipo_documento = %s,
        fecha_nacimiento = %s,
        lugar_residencia = %s,
        email = %s,
        telefono = %s,
        usuario = %s,
        contraseña = %s
    WHERE id_persona = %s
    """, (id_persona, nombres, apellidos, documento, id_tipo_documento, fecha_nacimiento, lugar_residencia, email, telefono, usuario, contraseña,id,))
    mysql.connection.commit()
    flash('Contacto actualizado satisfactoriamente')
    return redirect(url_for('index'))
    

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM persona WHERE Id_persona = {0}'.format(id))
    mysql.connection.commit()
    flash('Contacto removido satisfactoriamente')
    return redirect(url_for('index'))

if __name__=='__main__':
 app.run(port=3000, debug=True)
