# ORM sqlalchemy - Para poder usar las database que existen
# marshmallow - Permitira definir un schema para poder interactuar con la base de datos
# pymysql - Modulo para poder conectarse con la BD MySQl

# desde flask importare Flask
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Creando una variable se instancia de Flask pasando parametro de name
app = Flask(__name__)

# Configuracion Basica de donde se va conectar
#  Para poder configurar la conexion a SQL, dandole al app la config de la BD, su usuario,contraseña, etc
# mysql|DB + pymysql|El modulo de conexion instalado //|Direccion de la BD root|Usuario 123456|Contraseña localhost/flaskmysql|Direccion
# ['Recurso unico|donde esta la base de datos(Direccion)'] flaskmysql|Nombre de la base de datos(Schema se llama en el MySQL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/flaskmysql'
# Para que no dea un error, warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# El ORM crea las tablas por nosotros
# Pasar al ORM(SQLAlchemy) la configuracion que tiene el app, se guarda en la variable db para poder interactuar con la BD
db = SQLAlchemy(app)
# Instanciar el marshmallow para el schema
ma = Marshmallow(app)

# Definir la clase Task, heredando un Modelo que viene desde la base de datos, osea algunas propiedades que vienen de db
class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(70), unique=True)
    description = db.Column(db.String(100))
    
    def __init__(self, title, description):
        self.title = title
        self.description = description
        
db.create_all()
# Metodo Column para definir una columna
# Metodo Integer para indicarle que es tipo entero
# Se indica que es un PK
# Metodo String para indicarle que es tipo string, (longitud de cuantos caracteres puede soportar, tendra la propiedad Unique, no se puede repetir)

# def - Es el definicion o constructor de la clase Task, que tendra el nombre de __init__ que se ejecutara cada que se instancia esta clase, osea cuando se le invoca (como el constructor de Angular)

# Donde se recibe el tipico self, y los demas parametros de una funcion cualquiera
# self.title = title # Para usar los datos recibidos y poderlo asignarlos
# Esto solo lo define, no lo crea
# db.create_all() # Esto leera toda la clase, para que recien poder crear las columnas

class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description')

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

# Crear Schema, creando otra clase con (ma.Schema), importando el modulo ma, obteniendo de marshmallow un schema con su metodo Schema

# Definir los campos que tendra el Schema ('id', 'title', ...)

# Con task_schema, Se va instanciar TaskSchema, para que pueda ser usado en otras partes de la app.
# Para que cuando se quiera crear un solo Task, interactuar

# Para cuando se quiera crear varios Task, entonces con tasks_schema, con la propiedad many=True, para permitir tener multiples datos que obtendra multiples respuestas de la base datos

# ====== Ahora a definir las rutas ===== #

# Ruta, metodo Post
@app.route('/tasks', methods=['POST'])
def create_task():
    print(request.json)
    return 'reveived'

# Para crear una tarea el metodo create_task()
# Printeara el body que manda el back
# Retornara recibido si valida

# Para poder iniciar la aplicacion faltaria
# La condicional if, si estamos como la clase principal. Entonces app.run (ejecuta esta app.py) hara que se ejecute en un puerto y que se mostrara en consola y debug=True para que cada que se haga un cambio, se reinicia automaticamente.

if __name__ == "__main__":
    app.run(debug=True)