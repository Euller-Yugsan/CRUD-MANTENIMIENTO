import sys
from conexion import Conector

class DaoGrupo(Conector):
    def __init__(self):
        super().__init__()

    #Consultar
    def consultar(self,buscar):
        result=False
        try:
            sql="select*from grupo where descripcion like '"+str(buscar)+"%' order by id "
            self.conectar()
            self.conector.execute(sql)
            result=self.conector.fetchall()
            self.conn.commit ()
        except Exception as e:
            print("Error En La Consulta",e)
            self.conn.rollback()
        finally:
            self.cerrar()
        return result 
    #Insertar
    def ingresar(self, gru):
        correcto= True
        try:
            sql="insert into grupo(descripcion)values(%s)"
            self.conectar()
            self.conector.execute(sql,(gru.descripcion))
            self.conn.commit()
        except Exception as e:
            print("Error Al Insertar",e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()   
        return correcto

    #Modificar
    def modificar(self,gru):
        correcto=True
        try:
            sql="Update grupo set descripcion = %s  where id= %s"    
            self.conectar()
            self.conector.execute(sql,(gru.descripcion,gru.id))
            self.conn.commit()
        except Exception as e:
            print("Error Al Modificar",e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

       #Eliminar
    def eliminar(self,gru):
        correcto=True
        try:
            sql='delete from grupo where id=%s'
            self.conectar()
            self.conector.execute(sql,(gru.id))
            self.conn.commit()
        except Exception as e:
            print("Error Al Eliminar",e)
            correcto=False
            self.conn.rollback()    
        finally:
            self.cerrar()
        return correcto  

            




