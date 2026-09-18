# Importar la libreri pip install nicegui
from nicegui import ui

# Link de referencia https://docs.python.org/es/3/tutorial/datastructures.html#

# Definir Lista
item = [20, 50, 9, 45, 9, 78, 56, 3]

# Definit los metodos para la lista
def render_list():
    # Dibujar los cuadros de memoria de mi lista
    list_container.clear()
    with list_container:
        if not item:
            ui.label('Lista vacía').classes('text-gray-400 italic')
            return

        with ui.row().classes('items-center gap-2 flex-wrap'):
            for idx, val in enumerate(item):
                with ui.column().classes('items-center gap-1'):
                    # Muestra el valor de elemento
                    ui.label(str(val)).classes('w-16 h-16 flex items-center justify-center '
                        'bg-blue-800 text-white font-bold text-lg rounded-lg shadow-md')
                    # Muestra el indice del elemento
                    ui.label(f'[{idx}]*').classes('text-xs font-semibold text-slate-700')

# Metodo append
def do_append():
    if val_input.value is not None:
        item.append(val_input.value)
        render_list() 
        ui.notify('Valor agregado',color='secondary')
    else:
        ui.notify('Error: Debes introducir un valor para usar append().', color='warning')   

# Metodo Insert
def do_insert():
    if val_input.value is not None and idx_input is not None:
        idx = max(0, min(int(idx_input.value), len(item)))
        item.insert(idx, val_input.value)
        render_list()
        ui.notify('Valor insertado',color='info')
    else:
        ui.notify('Error: Faltan datos (Valor o Índice) para realizar insert().', color='warning')

# Metodo Pop
def do_pop():
    if not item:
        ui.notify('Error: La lista está vacía, no se puede hacer pop().', color='negative')
        return
    
    if idx_input is not None:
            idx = max(0, min(int(idx_input.value), len(item)))
            item.pop(idx-1)
            render_list()
            ui.notify('Valor eliminado',color='warning')

# Metodo Clear
def do_clear():
    item.clear()
    render_list()
    ui.notify('Lista eliminada',color='red')

#Metodo Count
def do_count():
    if val_input.value is not None:
        cantidad = item.count(val_input.value)
        ui.notify(f'El valor {val_input.value} aparece {cantidad} vez/veces en la lista.', color='info')
    else:
        ui.notify('Error: Debes ingresar un valor para contar.', color='warning')


#Metodo Reverse
def do_reverse():
    if not item:
        ui.notify('La lista está vacía.', color='warning')
        return
    item.reverse()
    render_list()
    

#Metodo Remove
def do_remove():
    if val_input.value is None:
        ui.notify('Error: Debes ingresar el valor que deseas eliminar.', color='warning')
        return
    
    val = val_input.value
    if val in item:
        item.remove(val)
        render_list()
        ui.notify('Elemento removido',color='red')
    else:
        ui.notify(f'Error: El valor {val} no se encuentra en la lista.', color='negative')
#Metodo Sort
def do_sort():
    if not item:
        ui.notify('La lista está vacía.', color='warning')
        return
    item.sort()
    render_list()
    ui.notify('Lista ordenada',color='purple')
# Interface
ui.page_title('Visualizador de Listas en Python con NiceGui')

# Contenedor Principal
with ui.column().classes('p-6 gap-6 w-full'):
    ui.label('Practica Grafica de una Lista').classes('text-2xl font-bold text-state-800')

    # Contenedor de los espacios de memoria
    with ui.card().classes('w-full p-4 min-h-[140px] bg-slate-50 border-slate-200'):
        list_container = ui.row().classes('w-full items-center')

    # Panel de Control (Las entradas y los Metodos)
    with ui.card().classes('w-full p-4 gap-4'):
        ui.label('OPERACIONES').classes('text-sm font-semibold text-slate-500')   

        # Contenedor de entrada de datos
        with ui.row().classes('gap-4 items-center'):
            val_input = ui.number('Valor', placeholder="Introduce un número").classes('w-40')
            idx_input = ui.number('Indice', value=0, min=0).classes('w-40')

        # Contenedor de botones de accion
        with ui.row():
            ui.button('append(x)', icon='add', color='secondary', on_click=do_append)
            ui.button('insert(i)', icon='add_circle', color='info', on_click=do_insert)
            ui.button('pop(i)', icon='remove', color='warning', on_click=do_pop)
            ui.button('remove(x)', icon='delete', color='red', on_click=do_remove)
            ui.button('sort()', icon='sort', color='purple', on_click=do_sort)
            ui.button('reverse()', icon='swap_vert', color='secondary', on_click=do_reverse)
            ui.button('count(x)', icon='123', color='grey', on_click=do_count)
            ui.button('clear()', icon='delete_sweep', color='red', on_click=do_clear)

render_list()
ui.run()