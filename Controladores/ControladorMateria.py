from Modelos.Materia import Materia
from Repositorios.RepositorioMateria import RepositorioMateria

class ControladorMateria():
    def __init__(self):
        self.repositorioMateria = RepositorioMateria()
        print("Creando controlador de Materia")

    def create(self, Materiaparaver):
        print("creando Materia")
        crearMateria = Materia(Materiaparaver)
        return self.repositorioMateria.save(crearMateria)

    def mostrarMateria(self, id):
        print("Mostrando el ID de la materia:" + str(id))
        materiaregistrada = Materia(self.repositorioMateria.findById(id))
        return materiaregistrada.__dict__

    def mostrarMaterias(self):
        print("Listar todas las Materias")
        return self.repositorioMateria.findAll()

    def delete(self, id):
        print("Se elimino una materia con el id: " + str(id))
        return self.repositorioMateria.delete(id)

    def update(self, id, Materiaparaver):
        print("Se Actualizo la materia con id: " + str(id))
        ActualizarMateria = Materia(self.repositorioMateria.findById(id))
        ActualizarMateria.nombre = Materiaparaver["nombre"]
        ActualizarMateria.creditos = Materiaparaver["creditos"]
        return self.repositorioMateria.update(id, ActualizarMateria)