#Nombre: Rosmery Aruni Paye RU: 200075568
from flask import Flask, request, jsonify
app = Flask(__name__)

tareas=[
    {'id': 1, 'tarea': 'Apredender Flask', 'completada': False},
    {'id': 2, 'tarea': 'Practicar con Flask', 'completada': False},
]
#GET-Obtener todas las tareas
@app.route('/api/tareas', methods=['GET'])
def listar_tareas():
    return jsonify(tareas)
#GET-Obtener una tarea especifica por ID
@app.route('/api/tareas/<int:tarea_id>', methods=['GET'])
def obtener_tarea(tarea_id):
    tarea = None
    for t in tareas:
        if t['id'] == tarea_id:
            tarea = t
            break
    if tarea:
        return jsonify(tarea)
    return jsonify({'error': 'Tarea no encontrada'}), 404

#post-crear una nueva tarea
@app.route('/api/tareas', methods=['POST'])
def crear_tarea():
    nueva_tarea = {
        'id': len(tareas) + 1,
        'tarea': request.json.get('tarea', ''),
        'completada': request.json.get('completada', False)
    }
    tareas.append(nueva_tarea)
    return jsonify(nueva_tarea), 201
#eliminar una tarea por ID
@app.route('/api/tareas/<int:tarea_id>', methods=['DELETE'])
def eliminar_tarea(tarea_id):
    global tareas
    tareas = [t for t in tareas if t['id'] != tarea_id]
    return jsonify({'mensaje': 'Tarea eliminada'}), 200

if __name__ == '__main__':
    app.run(debug=True)
