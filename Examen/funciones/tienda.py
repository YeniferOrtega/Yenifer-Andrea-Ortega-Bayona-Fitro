import os
import json
import funciones.globales as gf
import module.corefile as cg
import ui.uitiendas as uit

def newtienda():
    title = """
    *********************
    * registro de tiendas *
    *********************
    """
    gf.borrar_pantalla()
    print(title)
    nombre = input('ingresar nombre del producto')
    valorUni = input('ingrese valor del producto')
    stockmin = input('ingrese el minimo de stockmin')
    stockmax = input('ingrese maximo de producto')
    tienda ={
        "nombre" : nombre,
        "valorUni" : valorUni,
        "stockmin" : stockmin,
        "stockmax" : stockmax,
        "tienda" :tienda
    }

cg.AddData('data',nombre,tienda)
gf.tienda.get('data').update({nombre:tienda})
if(bool(input('desea registrar otro producto s(si) o enter(no)'))):
    newtienda(0)
else:
    uit.newtienda(0)

def searchData():
    criterio = input('Ingrese el Nro Identificacion del medico: ')
    data= gf.tienda.get('data').get(criterio)
    return data
  
def modifyData():
    datatienda = SearchData()
    nombre,valorUni,stockmin = datatienda.values()
    for key in datatienda.keys():
        if (key != 'identificacion' and key != ''):
            if(bool(input(f'Desea modificar el {key} s(si) o Enter No'))):
               datatienda[key] = input(f'Ingrese el nuevo valor para {key} :')
    gf.tienda.get('data').update({nombre:datatienda})
    cg.updatefi(gf.tienda)
    uit.Menutienda(0)
        





    
    

