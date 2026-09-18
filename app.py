from nicegui import ui
nombre=ui.input('ingresa tu nombre')
edad=ui.input('ingresa tu edad')
ui.page_title("Ejercicio")
def saludo():
    ui.label(f"Hola {nombre.value}, tu edad es {int(edad.value)}, aproximadamente naciste en el año {2026-int(edad.value)}")
with ui.column():
    ui.button('Presiona este boton',on_click=saludo)
ui.run()