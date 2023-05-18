from flask import Flask, request, render_template, session
from Cone import * #Importando conexion BD
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__) 

@app.route('/') 
def Inicio(): 
    return render_template('public/pagina.html')

@app.route('/pagina1.html') 
def Registro_Contactanos(): 
    return render_template('public/pagina1.html')

@app.route('/Registro.html') 
def Registro_Clientes(): 
    return render_template('public/Registro.html')

@app.route('/login.html') 
def login(): 
    return render_template('public/login.html')

@app.route('/Perifericos.html') 
def Perifericos(): 
    return render_template('public/Perifericos.html')

@app.route('/Perifericos.html') 
def Perifericosimg(): 
    return render_template('public/Perifericos.html')

@app.route('/hardware.html') 
def Hardware(): 
    return render_template('public/hardware.html')

@app.route('/hardware.html') 
def Hardwareimg(): 
    return render_template('public/hardware.html')

@app.route("/juegos.html")
def juegos():
    return render_template("public/juegos.html")

@app.route("/juegos.html")
def juegosimg():
    return render_template("public/juegos.html")

@app.route("/sobrenos.html")
def sobre_nos():
    return render_template("public/sobrenos.html")

msg=""

@app.route('/registroUsuario', methods=['GET', 'POST'])
def registroUsuario():
    msg =''
    if request.method == 'POST':
        Nombre              = request.form['Nombre']
        Apellido             = request.form['Apellido']
        Telefono              = request.form['Telefono']
        Email         = request.form['Email']
        Contrasena         = request.form['Contrasena' ]
        conexion_MySQLdb = connectionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)
        
        '''
        cursor.execute('INSERT INTO registro_usuario (Nombre, Apellido, Telefono , Email, Contrasena) VALUES (%s, %s, %s, %s, %s)', (Nombre, Apellido, Telefono , Email, Contrasena))
        ResultInsert = conexion_MySQLdb.commit()
        '''
            
        sql         = ("INSERT INTO registro_usuario (Nombre, Apellido, Telefono , Email, Contrasena) VALUES (%s, %s, %s, %s, %s)")
        valores     = (Nombre, Apellido, Telefono , Email, Contrasena)
        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()
        
        cursor.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        msg = 'Registro con exito'
        
        print(cursor.rowcount, "registro insertado")
        print("1 registro insertado", cursor.lastrowid)
        return render_template('public/Registro.html', msg='Formulario enviado')
    else:
        return render_template('public/Regisro.html', msg = 'Metodo HTTP incorrecto')


@app.route('/registrarForm', methods=['GET', 'POST'])
def registrarForm():
    msg =''
    if request.method == 'POST':
        Nombre              = request.form['Nombre']
        Email              = request.form['Email']
        Mensaje         = request.form['Mensaje']
        
        conexion_MySQLdb = connectionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)
        
        '''
        cursor.execute('INSERT INTO form_contacto (Nombre, Email, Mensaje) VALUES (%s, %s, %s)', (Nombre, Email, Mensaje))
        ResultInsert = conexion_MySQLdb.commit()
        '''
        sql         = ("INSERT INTO form_contacto (Nombre, Email, Mensaje) VALUES (%s, %s, %s)")
        valores     = (Nombre, Email, Mensaje)
        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()
        
        cursor.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        msg = 'Registro con exito'
        print(cursor.rowcount, "registro insertado")
        print("1 registro insertado, id", cursor.lastrowid)
        return render_template('public/pagina1.html', msg='Formulario enviado')
    else:
        return render_template('public/pagina1.html', msg = 'Metodo HTTP incorrecto')

@app.route('/loginUsuario', methods=['POST'])
def loginUser():
    conexion_MySQLdb = connectionBD()
    if 'conectado' in session:
        return render_template('public/pagina1.html')
    else:
        msg = ''
    if request.method == 'POST' and 'Email' in request.form and 'Contrasena' in request.form:
            Email        = str(request.form['Email'])
            Contrasena   = str(request.form['Contrasena'])
            
            # Comprobando si existe una cuenta
            cursor = conexion_MySQLdb.cursor(dictionary=True)
            cursor.execute("SELECT * FROM registro_usuario WHERE Email = %s AND Contrasena =%s",  [Email, Contrasena,])
            account = cursor.fetchone()
            
            if account:
                    # Crear datos de sesión, para poder acceder a estos datos en otras rutas 
                    msg = "Se ha iniciado sesión correctamente."
                    return render_template('public/pagina1.html', msjAlert = msg, typeAlert=1)                    
            else:
                    msg = 'Los datos ingresado son incorrectos, por favor verifica'
                    return render_template('public/login.html', msjAlert = msg, typeAlert=0)
if __name__ == '__main__': 
    app.run(debug=True, port=666) 



