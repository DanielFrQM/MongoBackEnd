from Repositorios.RepositorioInscripcion import RepositorioInscripcion
from Modelos.Inscripcion import Inscripcion


class ControladorInscripcion():
    def __init__(self):
        self.repositorioInscripcion = RepositorioInscripcion()
        print("Creando Controlado de Inscripcion")

    def create(self, infoInscripcion):
        print("crear Inscripcion")
        crearInscripcion = Inscripcion(infoInscripcion)
        return self.repositorioInscripcion.save(crearInscripcion)

    def mostrarInscripcion(self, id):
        print("Mostrando el Inscripcion con ID:"+str(id))
        elInscripcion = Inscripcion(self.repositorioInscripcion.findById(id))
        return elInscripcion.__dict__

    def mostrarInscripcions(self):
        print("Listar todos los Inscripcions")
        return self.repositorioInscripcion.findAll()

    def delete(self, id):
        print("Se elimino el Inscripcion con el id: "+str(id))
        return self.repositorioInscripcion.delete(id)

    def update(self,id,InscripcionDatos):
        print("Se Actualizo el Inscripcion con id: "+str(id))
        inscripcion = Inscripcion(self.repositorioInscripcion.findById(id))
        inscripcion.nombre = InscripcionDatos["nombre"]
        return self.repositorioInscripcion.update(id, inscripcion)