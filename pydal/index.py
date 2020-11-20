from flask import Flask, render_template,request,redirect,url_for,flash


from dataSource import *
app=Flask(__name__)

mysql = dataSource("127.0.0.1", "root", "", "parcial", "3306", "mysql")
sqlite = dataSource("", "", "", "parcial2", "", "sqlite")
app.secret_key='mysecretkey'




@app.route('/')
def index():
    mysqlquery = mysql.getData("select * from persona")
    sqlitequery = sqlite.getData("select * from persona")

    return render_template('index.html',contacts = mysqlquery,contacts2 = sqlitequery)
    
    
  

@app.route('/crear',methods=['POST'])
def crear():
    if request.method=='POST':
        Nombre=request.form['Nombre']
        Apellido=request.form['Apellido']
        Email=request.form['Email']
        Direccion=request.form['Direccion']
        Telefono=request.form['Telefono']
        mysql.query("INSERT INTO `persona`(`Nombre`, `Apellido`, `Email`) VALUES ('"+Nombre+"','"+Apellido+"','"+Email+"');")
        sqlite.query("INSERT INTO `persona` ('Direccion','Telefono' ) VALUES ('"+Direccion+"','"+Telefono+"');")
    #mysql.query("INSERT INTO `persona` ( ) VALUES (6);")
    flash('Usuario creado con exito')

    return redirect(url_for('index'))

@app.route("/eliminar/<string:id>")
def eliminar(id):
    mysql.query('DELETE FROM persona WHERE id='+id+'') 
    sqlite.query("DELETE FROM 'persona' WHERE id={0}".format(id))
    flash('Usuario eliminado')
    return redirect(url_for('index'))

@app.route('/editar/<id>')
def editar(id):
    qmysql = mysql.getData('SELECT * FROM persona WHERE id='+id+'')
    qsqlite = sqlite.getData('SELECT * FROM persona WHERE id='+id+'')
  #mysql.query('SELECT * FROM persona WHERE id='+id+'')
  #sqlite.query('SELECT * FROM persona WHERE id='+id+'')
    #print(qmysql[0])
    return render_template('editar.html',contact = qmysql[0],contact2 = qsqlite[0])


@app.route('/actualizar/<id>',methods=['POST'])
def actualizar(id):
    if request.method=='POST':
        Nombre=request.form['Nombre']
        Apellido=request.form['Apellido']
        Email=request.form['Email']
        Direccion=request.form['Direccion']
        Telefono=request.form['Telefono']
        mysql.query("UPDATE persona SET Nombre = '" +Nombre+ "', Apellido = '" +Apellido+ "', Email = '" +Email+ "' ")
        sqlite.query("UPDATE persona SET Direccion = '" +Direccion+ "', Telefono = '" +Telefono+ "' ")
        return redirect(url_for('index'))
if __name__== '__main__':
    app.run(port= 3000 , debug = True)
#


 