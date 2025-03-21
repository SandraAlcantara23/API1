class Nodo:
    def __init__(self, datos, hijos=None):
        self.datos = datos
        self.padre = None
        self.costo = None
        self.hijos = []
        if hijos:
            self.set_hijos(hijos)

    def set_hijos(self, hijos):
        if not isinstance(hijos, list):
            raise TypeError("hijos debe ser una lista de nodos")
        self.hijos = hijos
        for h in hijos:
            h.padre = self

    def get_hijos(self):
        return self.hijos

    def set_datos(self, datos):
        self.datos = datos

    def get_datos(self):
        return self.datos

    def set_costo(self, costo):
        self.costo = costo

    def get_costo(self):
        return self.costo

    def igual(self, nodo):
        return self.get_datos() == nodo.get_datos()

    def en_lista(self, lista_nodos):
        return any(self.igual(n) for n in lista_nodos)

    def _str_(self):
        return str(self.get_datos())

    def obtener_camino(self):
        nodo = self
        camino = []
        while nodo is not None:
            camino.append(nodo.get_datos())
            nodo = nodo.padre
        return camino[::-1]