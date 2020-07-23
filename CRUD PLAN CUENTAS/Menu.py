def menu(Opciones, titulo):
    print('-'*20)
    print('{}'.format(titulo))
    print('-'*20)
    for op in range(0, len(Opciones)):
        print("{}) {}".format(op, Opciones[op]))
    opc=input('Elija opcion [0...{}]:'.format(len(Opciones)-1))
    return opc


