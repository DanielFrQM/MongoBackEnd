from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorEstudiante import ControladorEstudiante
from Controladores.ControladorMateria import ControladorMateria
from Controladores.ControlDepartamento import ControladorDepartamento
from Controladores.ControladorInscripcion import ControladorInscripcion


app = Flask(__name__)
cors = CORS(app)

# Se realiza la creacion y manipulacion de los datos de estudiantes -----------------------

miControladorEstudiante = ControladorEstudiante()
miControladorMateria = ControladorMateria()
miControladorDepartamento = ControladorDepartamento()
miControladorInscripcion= ControladorInscripcion()

@app.route("/estudiantes",methods=['POST'])
def crearEstudiante():
    data = request.get_json()
    dictUsuario = miControladorEstudiante.create(data)
    return jsonify(dictUsuario)

@app.route("/estudiantes/<string:id>",methods=['GET'])
def getEstudiante(id):
    dictEstudiante = miControladorEstudiante.mostrarEstudiante(id)
    return jsonify((dictEstudiante))

@app.route("/estudiantes",methods=['GET'])
def getEstudiantes():
    dictEstudiantes = miControladorEstudiante.mostrarEstudiantes()
    return jsonify(dictEstudiantes)

@app.route("/estudiantes/<string:id>",methods=['PUT'])
def putEstudiante(id):
    data = request.get_json()
    dictEstudiante = miControladorEstudiante.update(id,data)
    return jsonify(dictEstudiante)

@app.route("/estudiantes/<string:id>",methods=['DELETE'])
def deleteEstudiante(id):
    dictEstudiante = miControladorEstudiante.delete(id)
    return jsonify(dictEstudiante)

# Se realizara la creacion y manipulacion de las materias -------------------

@app.route("/materia",methods=['POST'])
def crearMateria():
    data = request.get_json()
    dictMateria = miControladorMateria.create(data)
    return jsonify(dictMateria)

@app.route("/materia/<string:id>",methods=['GET'])
def getMateria(id):
    dictMateria = miControladorMateria.mostrarMateria(id)
    return jsonify((dictMateria))

@app.route("/materia",methods=['GET'])
def getMaterias():
    dictMaterias = miControladorMateria.mostrarMaterias()
    return jsonify(dictMaterias)

@app.route("/materia/<string:id>",methods=['PUT'])
def putMateria(id):
    data = request.get_json()
    dictMateria = miControladorMateria.update(id,data)
    return jsonify(dictMateria)

@app.route("/materia/<string:id>",methods=['DELETE'])
def deleteMateria(id):
    dictMateria = miControladorMateria.delete(id)
    return jsonify(dictMateria)

# se realiza el main para el apartado de Departamento ---------------------------

@app.route("/departamento",methods=['POST'])
def crearDepartamento():
    data = request.get_json()
    dictUsuario = miControladorDepartamento.create(data)
    return jsonify(dictUsuario)

@app.route("/departamento/<string:id>",methods=['GET'])
def getDepartamento(id):
    dictDepartamento = miControladorDepartamento.mostrarDepartamento(id)
    return jsonify((dictDepartamento))

@app.route("/departamento",methods=['GET'])
def getDepartamentos():
    dictDepartamentos = miControladorDepartamento.mostrarDepartamentos()
    return jsonify(dictDepartamentos)

@app.route("/departamento/<string:id>",methods=['PUT'])
def putDepartamento(id):
    data = request.get_json()
    dictDepartamento = miControladorDepartamento.update(id,data)
    return jsonify(dictDepartamento)

@app.route("/departamento/<string:id>",methods=['DELETE'])
def deleteDepartamento(id):
    dictDepartamento = miControladorDepartamento.delete(id)
    return jsonify(dictDepartamento)

# Se realiza la creacion y manipulacion de los datos de Inscripcion -----------------------

@app.route("/inscripcion",methods=['POST'])
def crearInscripcion():
    data = request.get_json()
    dictUsuario = miControladorInscripcion.create(data)
    return jsonify(dictUsuario)

@app.route("/inscripcion/<string:id>",methods=['GET'])
def getInscripcion(id):
    dictInscripcion = miControladorInscripcion.mostrarInscripcion(id)
    return jsonify((dictInscripcion))

@app.route("/inscripcion",methods=['GET'])
def getInscripcions():
    dictInscripcions = miControladorInscripcion.mostrarInscripcion()
    return jsonify(dictInscripcions)

@app.route("/inscripcion/<string:id>",methods=['PUT'])
def putInscripcion(id):
    data = request.get_json()
    dictInscripcion = miControladorInscripcion.update(id,data)
    return jsonify(dictInscripcion)

@app.route("/inscripcion/<string:id>",methods=['DELETE'])
def deleteInscripcion(id):
    dictInscripcion = miControladorInscripcion.delete(id)
    return jsonify(dictInscripcion)



# Se ejecuta un mensaje donde se nota la ejecucion del servidor ----------------------

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["mensaje"] = "Servidor ejecutándose"
    return jsonify(json)


def loadFileConfig():
    with open("config.json") as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Servidor corriendo en: " + "host: " + dataConfig["url-backend"] + " puerto: " + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig['port'])

