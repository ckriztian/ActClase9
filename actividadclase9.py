## video: https://youtu.be/DiwI9uCAQO8 
## video: https://youtu.be/DiwI9uCAQO8 

lista = []
lista_con_fecha = []

class TareaGeneral:
    def __init__(self, tarea, descripcion, prioridad):
        self.tarea = tarea
        self.descripcion = descripcion
        self.prioridad = prioridad
    def __str__(self):
        return f"Nombre: {self.tarea}, Descripción: {self.descripcion}, Prioridad: {self.prioridad}"

class TareaConFecha(TareaGeneral):
    def __init__(self, tarea, descripcion, prioridad, fecha):
        super().__init__(tarea, descripcion, prioridad)
        self.fecha = fecha
    def __str__(self):
        return f"Nombre: {self.tarea}, Descripción: {self.descripcion}, Prioridad: {self.prioridad}, Fecha: {self.fecha}"

def menu():
    opcion = 0
    while opcion != 5:
        print('***** Lista de tareas *****')
        print('Elegir una de las opciones')
        print('1. Agregar Tarea')
        print('2. Agregar Tarea con Fecha')
        print('3. Mostrar Tarea')
        print('4. Eliminar Tarea')
        print('5. Salir \n')
        opcion = int(input("* Elige una opcion: "))
        if opcion == 1:
            agregar_tarea()
        elif opcion == 2:
            agregar_tarea_con_fecha()
        elif opcion == 3:
            mostrar_tarea()
        elif opcion == 4:
            eliminar_tarea()
        elif opcion == 5:
            salir()
        else:
            print("Opción no válida. Por favor elija una opción entre 1 y 5.")

def agregar_tarea():
    print('\n***** Insertando tarea *****')
    tarea = input("Inserte la tarea: ")
    descripcion = input("Descripcion de la tarea: ")
    prioridad = input("Prioridad de la tarea (Alta,Media,Baja): ")
    task = TareaGeneral(tarea, descripcion, prioridad)
    lista.append(task)
    print('Tarea agregada!!\n')

def agregar_tarea_con_fecha():
    print('\n***** Insertando tarea *****')
    tarea = input("Inserte la tarea: ")
    descripcion = input("Descripcion de la tarea: ")
    prioridad = input("Prioridad de la tarea (Alta,Media,Baja): ")
    fecha = input("Fecha de fin de tarea: ")
    task = TareaConFecha(tarea, descripcion, prioridad, fecha)
    lista_con_fecha.append(task)
    print('Tarea agregada!!\n')

def mostrar_tarea():
    print('***** Mostrar la tarea agregada *****')
    if not lista and not lista_con_fecha:
        print("No hay tareas agregadas!!!!\n")
    else:
        for task in lista:
            print(task)
        for task in lista_con_fecha:
            print(task)

def eliminar_tarea():
    print('***** Eliminar la tarea seleccionada *****')
    eliminar = input("Inserte la tarea que desea eliminar: ")
    for task in lista:
        if task.tarea == eliminar:
            lista.remove(task)
            print('Tarea eliminada!!\n')
            return
    for task in lista_con_fecha:
        if task.tarea == eliminar:
            lista_con_fecha.remove(task)
            print('Tarea eliminada!!\n')
            return
    print("Tarea no encontrada.\n")

def salir():
    print('Adios. Lista de tarea.')

menu() 

## video: https://youtu.be/DiwI9uCAQO8 
