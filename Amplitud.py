#inicializar clase nodo
class Nodo:
    def __init__(self,datos, hijos=None):
        self.datos = datos
        self.hijos = None
        self.padre = None
        self.costo = None
        self.set_hijos(hijos)
#Asignando al nodo, la lista de hijos(que son pasados como parametros)
def set_hijos(self,hijos):
    self.hijos = hijos
    if self.hijos != None:
        for h in self.hijos:
            h.padre = self
#Esto Regresa una lista con los hijos de nodos
def get_hijos(self):
    return self.hijos
#Esto Reregsa el nodo padre
def get_padre(self):
    return self.padre
#Asigna el nodo padre de este nodo
def set_padre(self, padre):
    set_padre = padre
#Asigna un dato al nodo
def set_datos(self, datos):
    self.datos = datos
#Devuleve el dato alamcenado al nodo
def get_datos(self):
    return self.datos

def set_costo(self, costo):
    self.costo = costo

def get_costo(self):
    return self.costo
#Este devuelve un verdadero, si el dato contenido en el nodo es igual al nodo pasado como parametro
def igual(self, nodo):
    if self.get_datos() == nodo.get_datos():
        return True
    else:
        return False
#Devuelve verdadero si el dato contiene el nodo es igual a alguno de los nodos contenidos en la lista de nodos pasados como parametros.
def en_lista(self,lista_nodos):
    en_la_lista = False
    for n in lista_nodos:
        if self.igual(n):
            en_la_lista = True
    return en_la_lista

def __str__(self):
    return str(self.get_datos())