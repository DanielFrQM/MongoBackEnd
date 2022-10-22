from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

#import pymongo
#import certifi
#ca = certifi.where()
#cliente = pymongo.MongoClient("mongodb+srv://daniefrqm:Danielelrey1@cluster0.bxdr7uy.mongodb.net/?retryWrites=true&w=majority",  tlsCAFile=ca)
#db = cliente.test
#print(db)
#baseDatos = cliente['db-registro-academico']
#print(baseDatos.list_collection_names())

from Controladores.ControladorEstudiante import ControladorEstudiante
from Controladores.ControladorMateria import ControladorMateria


app = Flask(__name__)
cors = CORS(app)

# Se realiza la creacion y manipulacion de los datos de estudiantes -----------------------

miControladorEstudiante = ControladorEstudiante()
miControladorMateria = ControladorMateria()

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

