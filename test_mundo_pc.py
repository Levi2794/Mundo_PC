from teclado import Teclado
from monitor import Monitor
from raton import Raton
from computadora import Computadora
from orden import Orden

teclado_1 = Teclado('HP', 'USB')
monitor_1 = Monitor('HP', 27)
raton_1 = Raton('HP', 'USB')
computadora_1 = Computadora('HP', monitor_1, teclado_1, raton_1)

teclado_2 = Teclado('Logitech', 'Wi-Fi')
monitor_2 = Monitor('Asus', 27)
raton_2 = Raton('Logitech', 'USB')
computadora_2 = Computadora('Lenovo', monitor_2, teclado_2, raton_2)

teclado_3 = Teclado('Gamer', 'Bluetooth')
monitor_3 = Monitor('Gamer', 32)
raton_3 = Raton('Gamer', 'Bluetooth')
computadora_3 = Computadora('Gamer', monitor_3, teclado_3, raton_3)

computadoras1 = [computadora_1, computadora_2]
orden1 = Orden(computadoras1)
#print(orden1)

orden1.agregar_computadora(computadora_3)
print(orden1)
