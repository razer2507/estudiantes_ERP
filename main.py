from basedatos import db
from logica.helpers import logica
from gui.ventana_principal import VentanaPrincipal


base_datos = db()

reglas = logica(base_datos)

menu_principal = VentanaPrincipal(reglas)
