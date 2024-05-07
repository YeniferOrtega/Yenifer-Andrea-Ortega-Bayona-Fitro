from module import corefile as cf
import funciones.globales as fg
import module.corefile as cg
import ui.uitiendas as uit

def main():
     cf.MY_DATABASE_ = 'data/tiendas.json'
     cf.checkFile(fg.tienda)
     op = 0
     MainMenu(op)

def MainMenu(op):
      fg.borrar_pantalla()
      title = """
    *************************
    * ALMINISTRADOR DE TIENDA *
    *************************
    """
      MainMenuOp = "1.agrega 2.\n editar 3.\n eliminar 4\n salir "
      if (op != 4):
            print(title)
            print(MainMenuOp)
            try:
                opcion = int(input(':) '))
            except ValueError:
                print('error en la occion ingresada')
                fg.pausar_pantalla()
                MainMenu(0)
            else:
                match (opcion):
                      case 1: 
                            uit.Menutienda(0)
                      case 2: 
                        print('opcion ingresada no pertenece al menu de opciones')
                        fg.borrar_pantalla()

                        MainMenu(0)
                    
                           
                         
    




    