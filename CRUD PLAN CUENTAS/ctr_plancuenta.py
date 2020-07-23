from dao_plancuenta import DaoPlancuenta
from mod_plancuenta import ModCuenta
from dao_grupo import DaoGrupo

class  CtrPlancuenta:
    def __init__ (self, cuen=None):
        self.cuenta=cuen 

    def consultar(self, buscar):
        objDao=DaoPlancuenta()
        return objDao.consultar(buscar) 

    def insertar(self,cuen):
        objDao=DaoPlancuenta()
        return objDao.insertar(cuen)

    def modificar(self ,cuen):
        objDao=DaoPlancuenta()
        return  objDao.modificar(cuen) 

    def eliminar(self,cuen):
        objDao=DaoPlancuenta()
        return objDao.eliminar(cuen)
    

    def consultargrupo(self):
        objDao=DaoPlancuenta()
        return objDao.codigogrupo()

    def consultarcuenta(self):
        objDao=DaoPlancuenta()
        return objDao.codigocuenta()

 






