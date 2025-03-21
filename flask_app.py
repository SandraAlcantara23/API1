from flask import Flask, request, render_template
from arbol import Nodo

app = Flask(__name__)

def buscar_solucion_BFS_rec(nodo_inicial, solucion, visitados):
    print(f"Visitando nodo: {nodo_inicial.get_datos()}")
    visitados.append(nodo_inicial.get_datos())
    if nodo_inicial.get_datos() == solucion:
        print("¡Solución encontrada!")
        return nodo_inicial

    dato_nodo = nodo_inicial.get_datos()

    # Crear los hijos sin asignar el padre en la instanciación
    hijo_izquierdo = Nodo([dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]])
    hijo_central   = Nodo([dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]])
    hijo_derecho   = Nodo([dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]])

    # Asignar manualmente el padre
    hijo_izquierdo.padre = nodo_inicial
    hijo_central.padre   = nodo_inicial
    hijo_derecho.padre   = nodo_inicial

    # Definir la lista de hijos en el nodo actual
    nodo_inicial.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])

    for nodo_hijo in nodo_inicial.get_hijos():
        if nodo_hijo.get_datos() not in visitados:
            sol = buscar_solucion_BFS_rec(nodo_hijo, solucion, visitados)
            if sol is not None:
                return sol

    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    camino = None
    if request.method == 'POST':
        estado_inicial_str = request.form.get('estado_inicial')
        estado_final_str   = request.form.get('estado_final')
        try:
            # Convertir cadenas como "4,3,2,1" en listas de enteros
            estado_inicial = [int(x.strip()) for x in estado_inicial_str.split(',')]
            estado_final   = [int(x.strip()) for x in estado_final_str.split(',')]
        except Exception as e:
            return f"Error al convertir los estados: {str(e)}"

        nodo_inicial = Nodo(estado_inicial)
        visitados = []
        nodo_solucion = buscar_solucion_BFS_rec(nodo_inicial, estado_final, visitados)
        if nodo_solucion:
            camino = nodo_solucion.obtener_camino()
        else:
            camino = "No se encontró solución."

    return render_template('index.html', camino=camino)

if __name__ == '__main__':
    app.run(debug=True)