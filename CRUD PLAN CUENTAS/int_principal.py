from ctr_grupo import CtrGrupo
from ctr_plancuenta import CtrPlancuenta
from mod_grupo import ModGrupo
from mod_plancuenta import ModCuenta
from Menu import menu
import os 
ctr=CtrGrupo()
ctrp=CtrPlancuenta()
#METODOS GRUPOS
def consultar():
    buscar=input('Ingrese Nombre A Buscar: ')
    cli=ctr.consultar(buscar)
    print('\n\tCodigo\tDescripcion')
    for cursor in cli:
        print('\n\t{}\t{}'.format(cursor[0],cursor[1]))

def modificar():
    cli=ctr.consultar('')
    print('\n\tCodigo\tDescripcion')
    for cursor in cli:
        print('\n\t{}\t{}'.format(cursor[0],cursor[1]))
    codigo=input('\nIngrese Codigo A Modificar: ')
    descripcion=input('Ingrese Nueva Descripcion: ')
    cli=ModGrupo(cod=codigo,desc=descripcion)
    if ctr.modificar(cli):
        print('Registro Modificado')
    else:
        print('Error Al Modificar')   

def insertar(rango):
        descripcion=input('Ingrese Descripcion: ')
        cli=ModGrupo(desc=descripcion)
        if ctr.ingresar(cli):
            print('Registro Guardado')
        else:
            print('Error Al Guardar')  

def eliminar():
    cli=ctr.consultar('')
    print('\n\tCodigo\tDescripcion')
    for cursor in cli:
        print('\n\t{}\t{}'.format(cursor[0],cursor[1]))
    codigo=input('\nIngrese Codigo A Eliminar: ')
    cli=ModGrupo(cod=codigo)
    if ctr.eliminar(cli):
        print('Registro Eliminado')
    else:
        print('Error Al Eliminar')                  

#METODOS PLAN CUENTA
#Consultar
def consultarp():
    buscar=input('Ingrese Nombre A Buscar: ')
    cli=ctrp.consultar(buscar)
    print('\n\tId\tCodigo\tGrupo\tDescripcion\tNaturaleza\tEstado')
    for plan in cli:
        print('\n\t{}\t{}\t{}\t{}\t\t{}\t\t{}'.format(plan[0],plan[1],plan[2],plan[3],plan[4],plan[5]))
#Insertar

def insertarp(rango):
    for i in range(int(rango)):
        cod=ctrp.consultarcuenta()
        if len(cod)==0:
            codigo=input('Ingrese Codigo 01: ')
        else:
            codigo=input('Ultimo Codigo'+str("{}".format(cod[0]))+',ingresar el siguiente codigo: ') 
        grupo=ctrp.consultargrupo()
        for gru in grupo:
            print(gru[0],gru[1])
        grupo=input('Digite Numero De Grupo: ')
        descrip=input('Ingrese Descripcion Del Plan: ')
        natura=input('Ingrese Naturaleza Del Plan A/D: ' )
        estado=input('Digite Estado De Plan 1=True/0=False: ')
        planc=ModCuenta(codi=codigo,grup=grupo,desc=descrip,nat=natura,est=estado)
        if ctrp.insertar(planc):
            print('Registro Correcto')        
        else:
            print('Erro Al Insertar') 
#Eliminar
def eliminarp():
    cli=ctrp.consultar('')
    print('\n\tId\tCodigo\tGrupo\tDescripcion\tNaturaleza\tEstado')
    for plan in cli:
        print('\n\t{}\t{}\t{}\t{}\t\t{}\t\t{}'.format(plan[0],plan[1],plan[2],plan[3],plan[4],plan[5]))
    codp=input('\nIngrese Id Que Desea Borrar: ')
    cli=ModCuenta(cod=codp)
    if ctrp.eliminar(cli):
        print("Registro Eliminado")
    else:
        print("Error Al Eliminar")    

#Modificar
def modificarp():
    cli=ctrp.consultar('')
    print('\n\tId\tCodigo\tGrupo\tDescripcion\tNaturaleza\tEstado')
    for plan in cli:
        print('\n\t{}\t{}\t{}\t{}\t\t{}\t\t{}'.format(plan[0],plan[1],plan[2],plan[3],plan[4],plan[5]))
    idP=input('\nIngrese Id A Modificar: ')
    grupo=input('Ingrese Nuevo Grupo: ')
    descrip=input('Ingrese Nueva Descripcion: ')
    natura=input('Ingrese Nueva Naturaleza Del Plan A/D: ')
    esta=input('Ingrese Nuevo Estado 1=True/0=False: ')
    cli=ModCuenta(grup=grupo,desc=descrip,nat=natura,est=int(esta),cod=idP)
    if ctrp.modificar(cli):
        print('Registro Modificado')
    else:
        print('Error Al Modificar')    


#MENU PRINCIPAL

def ejecutar_menuprincipal():
    opc=''
    while True:
        opc=str(menu(
            ['Grupos de cuentas','Plan de cuentas','Salir'],'  *CRUD CUENTAS*'))
        if opc=='0':  
            os.system('cls') 
            ejecutar_menugrupo()       
        elif opc=='1':
            os.system('cls') 
            ejecutar_menuplan()
        elif opc== '2':
            print('GRACIAS POR PREFERIRNOS')
            input('PRESIONE UNA TECLA PARA CONTINUAR')
            break
        elif opc!='2':
            print('Seleciona Una Opcion Valida')
        input('PRESIONE UNA TECLA PARA CONTINUAR')   
        os.system('cls') 
        
#MENU GRUPO

def ejecutar_menugrupo():
    opc=''
    while True:
        opc=str(menu(
            ['Ingresar','Consultar','Modificar','Eliminar','Menu Principal'],'*MENU GRUPO DE CUENTAS*'))
        if opc=='0':
            print('\nINGRESAR') 
            valor=input('Ingrese Cantidad De Datos A Ingresar: ')
            insertar(valor)
        elif opc=='1':
            print('\nCONSULTAR\n')
            consultar()
        elif opc=='2':
            print('\nMODIFICAR') 
            modificar()
        elif opc=='3':
            print('\nELIMINAR')   
            eliminar()     
        elif opc=='4':
            os.system('cls')  
            ejecutar_menuprincipal() 
            break      
        elif opc!='4':
            print('Seleciona Una Opcion Valida')
        input('\nPRESIONE UNA TECLA PARA CONTINUAR')   
        os.system('cls') 

#MENU PLAN

def ejecutar_menuplan():
    opc=''
    while True:
        opc=str(menu(
            ['Ingresar','Consultar','Modificar','Eliminar','Menu Principal'],'*MENU PLAN CUENTAS'))
        if opc=='0':
            print('\nINGRESAR')
            valor=input('Ingrese Cantidad De Datos A Ingresar: ')
            insertarp(valor)
        elif opc=='1':
            print('\nCONSULTAR')  
            consultarp()      
        elif opc=='2':
            print('\nMODIFICAR')  
            modificarp() 
        elif opc=='3':
            print('\nELIMINAR') 
            eliminarp()   
        elif opc=='4':
            os.system('cls')  
            ejecutar_menuprincipal()   
            break                     
        elif opc!='4':
            print('Seleciona Una Opcion Valida')
        input('\nPRESIONE UNA TECLA PARA CONTINUAR')   
        os.system('cls')      
         
os.system('cls')  
ejecutar_menuprincipal() 
