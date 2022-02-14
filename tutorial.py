# https://www.google.com/url?sa=i&url=http%3A%2F%2Fwww.maestrosdelweb.com%2Fguia-python-plantilla-html-lista-precios%2F&psig=AOvVaw101KzNJDXYrgi3ARCJhFY2&ust=1644945949087000&source=images&cd=vfe&ved=0CAwQjhxqFwoTCODJg6rb__UCFQAAAAAdAAAAABBK


# ESTRUCTURAS DE DATOS - DICCIONARIO
d1 = {
  "Nombre": "Sara",
  "Edad": 27,
  "Documento": 1003882
}

d2 = dict([
      ('Nombre', 'Sara'),
      ('Edad', 27),
      ('Documento', 1003882),
])

d3 = dict(Nombre='Sara',
          Edad=27,
          Documento=1003882)

print(d3)

print(d1['Nombre'])     #Sara
print(d1.get('Nombre')) #Sara

#SETEAR
d1['Nombre'] = "Laura"

#AGREGAR
# Si el key al que accedemos no existe, se añade automáticamente.
# key: value
d1['Direccion'] = "Calle 123"

# Imprime los key del diccionario
for x in d1:
    print(x)
    
# Imprime los value del diccionario
for x in d1:
    print(d1[x])
    
# Imprime los key y value del diccionario
for x, y in d1.items():
    print(x, y)

##############################################
# Diccionarios anidados
anidado1 = {"a": 1, "b": 2}
anidado2 = {"a": 1, "b": 2}
d = {
  "anidado1" : anidado1,
  "anidado2" : anidado2
}
print(d)
#{'anidado1': {'a': 1, 'b': 2}, 'anidado2': {'a': 1, 'b': 2}}

##############################################
# Métodos diccionarios Python
d = {'a': 1, 'b': 2}
d.clear()
print(d) #{}

# El segundo parámetro es opcional, y en el caso de proporcionarlo es el valor a devolver si no se encuentra la key.
d = {'a': 1, 'b': 2}
print(d.get('a')) #1
print(d.get('z', 'No encontrado')) #No encontrado

# items()
d = {'a': 1, 'b': 2}
it = d.items()
print(it)             #dict_items([('a', 1), ('b', 2)])
print(list(it))       #[('a', 1), ('b', 2)]
print(list(it)[0][0]) #a

# El método keys() devuelve una lista con todas las keys del diccionario.
d = {'a': 1, 'b': 2}
k = d.keys()
print(k)       #dict_keys(['a', 'b'])
print(list(k)) #['a', 'b']

# El método values() devuelve una lista con todos los values o valores del diccionario.
d = {'a': 1, 'b': 2}
print(list(d.values())) #[1, 2]

# El método pop() busca y elimina la key que se pasa como parámetro y devuelve su valor asociado. Daría un error si se intenta eliminar una key que no existe.
d = {'a': 1, 'b': 2}
d.pop('a')
print(d) #{'b': 2}

# También se puede pasar un segundo parámetro que es el valor a devolver si la key no se ha encontrado. En este caso si no se encuentra no habría error.
d = {'a': 1, 'b': 2}
d.pop('c', -1)
print(d) #{'a': 1, 'b': 2}


# El método update() se llama sobre un diccionario y tiene como entrada otro diccionario. Los value son actualizados y si alguna key del nuevo diccionario no esta, es añadida.
d1 = {'a': 1, 'b': 2}
d2 = {'a': 0, 'd': 400}
d1.update(d2)
print(d1)
#{'a': 0, 'b': 2, 'd': 400}
















###############################################
# PARAMETROS FUNCIONES ARGS - KARGS
def suma(*args):
    s = 0
    for arg in args:
        s += arg
    return s


print('resultado:', suma(1, 3, 4, 2))




def suma(**kwargs):
    s = 0
    for key, value in kwargs.items():
        print(key, "=", value)
        s += value
    return s


print('resultado:', suma(a=3, b=10, c=3))
