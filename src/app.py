# ORM sqlalchemy - Para poder usar las database que existen
# marshmallow - Permitira definir un schema para poder interactuar con la base de datos
# pymysql - Modulo para poder conectarse con la BD MySQl

# desde flask importare Flask
from flask import Flask, request, jsonify
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
# Metodo Column para definir una columna - db.Column
# Se indica que es un PK - primary_key = True
# Metodo Integer para indicarle que es tipo entero - db.Integer
# Metodo String para indicarle que es tipo string, (longitud de cuantos caracteres puede soportar, tendra la propiedad Unique, no se puede repetir)

# def - Es el definicion o constructor de la clase Task, que tendra el nombre de __init__ que se ejecutara cada que se instancia esta clase, osea cuando se le invoca (como el constructor de Angular)

# Donde se recibe el tipico self, y los demas parametros de una funcion cualquiera
# Para usar los datos recibidos y poderlo asignarlos - self.title = title 
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

# Para cuando se quiera crear varios Task, entonces con tasks_schema, con la propiedad many=True,
# para permitir tener multiples datos que obtendra multiples respuestas de la base datos

# ====== Ahora a definir las rutas ===== #

# Ruta, metodo Post
@app.route('/tasks', methods=['POST'])
def create_task():
    print(request.json)
    # Se extrae los datos del Request, y se asigna a variables
    title = request.json['title']
    description = request.json['description']
    
    # Se crea el cascaron de una Tarea dando los datos de las variables, osea solo se arma el Model, la tarea
    new_task = Task(title, description)
    # Se agrega a la Base de datos
    db.session.add(new_task)
    # Terminar con la operacion de agregar
    db.session.commit()
    
    # jsonify - Convierte a json, eso retornaremos
    return task_schema.jsonify(new_task)
    # return 'reveived'

# Para crear una tarea el metodo create_task()
# Printeara el body que manda el back
# Retornara recibido si valida

# Para poder iniciar la aplicacion faltaria
# La condicional if, si estamos como la clase principal. Entonces app.run (ejecuta esta app.py) hara que se ejecute en un puerto y que se mostrara en consola y debug=True para que cada que se haga un cambio, se reinicia automaticamente.

# Solo es necesario crear la Base de Datos, ya que las tablas se crean aqui

# Ruta, metodo Get
@app.route('/tasks', methods=['GET'])
def get_tasks():
    # Consultar el modelo de datos - All retornara todas las tareas, de esa modelo (Tabla)
    # Se obiiene todas las tablas
    all_tasks = Task.query.all() 
    # Obtendra un Listado del resultado
    result = tasks_schema.dump(all_tasks)
    # Para poder mostrarlo como Json
    return jsonify(result)

# Ruta, metodo Get
@app.route('/tasks/<id>', methods=['GET'])
def get_task(id):
    # Parametro de la funcion con el mismo nombre
    # Para traer uno en especifico, con el metodo get se envia el parametro unico
    task = Task.query.get(id) # Query como metodo para poder extraer
    # Si no funciona jsonify(result), la otra manera es asi
    return task_schema.jsonify(task)

# Ruta, metodo Post
@app.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
    # Encuentras la fila de la tarea
    task = Task.query.get(id)
    
    # Extraes los datos del Req
    title = request.json['title']
    description = request.json['description']
    
    # Reemplazas la fila de la tarea extraida
    task.title = title
    task.description = description
    
    db.session.commit()
    return task_schema.jsonify(task)

# Ruta, metodo Post
@app.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    
    # Te mostrara la tarea que acabas de eliminar
    return task_schema.jsonify(task)

# Ruta, metodo Post
@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome API'})

if __name__ == "__main__":
    app.run(debug=True)