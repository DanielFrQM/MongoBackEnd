from Modelos.Estudiante import Estudiante
from Repositorios.RepositorioEstudiante import RepositorioEstudiante

class ControladorEstudiante():
    def __init__(self):
        self.repositorioEstudiante = RepositorioEstudiante()
        print("Creando Controlado de Estudiante")

    def create(self, estudianteDatos):
        print("crear estudiante")
        crearEstudiante = Estudiante(estudianteDatos)
        return self.repositorioEstudiante.save(crearEstudiante)

    def mostrarEstudiante(self, id):
        print("Mostrando el estudiante con ID:"+str(id))
        elEstudiante = Estudiante(self.repositorioEstudiante.findById(id))
        return elEstudiante.__dict__

    def mostrarEstudiantes(self):
        print("Listar todos los estudiantes")
        return self.repositorioEstudiante.findAll()

    def delete(self, id):
        print("Se elimino el estudiante con el id: "+str(id))
        return self.repositorioEstudiante.delete(id)

    def update(self,id,estudianteDatos):
        print("Se Actualizo el estudiante con id: "+str(id))
        estudiante = Estudiante(self.repositorioEstudiante.findById(id))
        estudiante.nombre = estudianteDatos["nombre"]
        estudiante.apellido = estudianteDatos["apellido"]
        estudiante.cedula = estudianteDatos["cedula"]
        return self.repositorioEstudiante.update(id, estudiante)

