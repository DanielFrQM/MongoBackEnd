from Repositorios.RepositorioDepartamento import RepositorioDepartamento
from Modelos.Departamento import Departamento


class ControladorDepartamento():
    def __init__(self):
        self.repositorioDepartamento = RepositorioDepartamento()
        print("Creando Controlado de Departamento")

    def create(self, infoDepartamento):
        print("crear Departamento")
        crearDepartamento = Departamento(infoDepartamento)
        return self.repositorioDepartamento.save(crearDepartamento)

    def mostrarDepartamento(self, id):
        print("Mostrando el Departamento con ID:"+str(id))
        elDepartamento = Departamento(self.repositorioDepartamento.findById(id))
        return elDepartamento.__dict__

    def mostrarDepartamentos(self):
        print("Listar todos los Departamentos")
        return self.repositorioDepartamento.findAll()

    def delete(self, id):
        print("Se elimino el Departamento con el id: "+str(id))
        return self.repositorioDepartamento.delete(id)

    def update(self,id,DepartamentoDatos):
        print("Se Actualizo el Departamento con id: "+str(id))
        departamento = Departamento(self.repositorioDepartamento.findById(id))
        departamento.nombre = DepartamentoDatos["nombre"]
        return self.repositorioDepartamento.update(id, departamento)

