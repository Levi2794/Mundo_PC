from teclado import Teclado
from monitor import Monitor
from raton import Raton

class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return '''
            {}: {}
            Monitor: {}
            Teclado: {}
            Raton: {}
        '''.format(self._nombre,self._id_computadora,self._monitor,self._teclado,self._raton)

if __name__ == '__main__':
    teclado_1 = Teclado('HP', 'USB')
    monitor_1 = Monitor('HP', 27)
    raton_1 = Raton('HP', 'USB')
    computadora_1 = Computadora('HP', monitor_1, teclado_1, raton_1)
    print(computadora_1)
    teclado_2 = Teclado('Logitech', 'Wi-Fi')
    monitor_2 = Monitor('Asus', 27)
    raton_2 = Raton('Logitech', 'USB')
    computadora_2 = Computadora('Lenovo', monitor_2, teclado_2, raton_2)
    print(computadora_2)


