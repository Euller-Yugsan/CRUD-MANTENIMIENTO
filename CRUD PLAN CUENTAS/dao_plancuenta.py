import sys
from conexion import Conector

class DaoPlancuenta(Conector):
    def __init__(self):
        super().__init__()

    #Consulta
    def consultar(self , buscar):
        result=False
        try :
            sql= sql ="SELECT pl.id,pl.codigo  ,gru.descripcion  ,pl.descripcion ,pl.naturaleza ,case pl.estado when 1 then 'True' ELSE  'False'  END  FROM plancuenta pl JOIN grupo gru ON pl.grupo=gru.id where pl.descripcion like'"+str(buscar)+"%' order by id"
            self.conectar()
            self.conector.execute(sql)
            result=self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print("Error En La Consulta", e)
            self.conn.rollback()
        finally:
            self.cerrar()
        return result
    
    #Ingresar
    def insertar(self, cuen):
        correcto= True
        try:
            sql="insert into plancuenta (codigo, grupo, descripcion, naturaleza, estado) values (%s, %s, %s, %s, %s)"
            self.conectar()
            self.conector.execute(sql,(cuen.codigo, cuen.grupo, cuen.descripcion, cuen.naturaleza, cuen.estado))
            self.conn.commit()
        except Exception as e:
            print("Error Al Insertar", e)
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto
    
    #Modificar
    def modificar(self, cuen):
        correcto= True
        try:
            sql="update plancuenta set grupo=%s, descripcion=%s, naturaleza=%s, estado=%s where id = %s"
            self.conectar()
            self.conector.execute(sql,(cuen.grupo, cuen.descripcion, cuen.naturaleza, cuen.estado, cuen.id))
            self.conn.commit()
        except Exception as e:
            print("Error Al Modificar", e)
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto  

    #Eliminar
    def eliminar(self, cuen):
        correcto = True
        try:
            sql="DELETE FROM  plancuenta where id = %s"
            self.conectar()
            self.conector.execute(sql,(cuen.id))
            self.conn.commit()
        except Exception as e:
            print("Error Al Eliminar", e)
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    #Codigo
    def codigogrupo(self)    :
        result=False
        try:
            sql="select id , descripcion from grupo order by id"
            self.conectar()
            self.conector.execute(sql)
            result=self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print("Error",e)
            self.conn.rollback()
        finally:
            self.cerrar()
        return result   

    def codigocuenta(self):
        result=False
        try:
            sql="select codigo from plancuenta order by codigo desc limit 1"
            self.conectar()
            self.conector.execute(sql)
            result=self.conector.fetchall()
            self.conn.commit()
        except Exception  as e:
            print("Error",e)
            self.conn.rollback()
        finally:
            self.cerrar()
        return result                         

         




