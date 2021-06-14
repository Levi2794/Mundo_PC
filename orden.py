class Orden:
    contador_ordenes = 0
    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self._ide_ordenes = Orden.contador_ordenes
        self._computadoras = computadoras

    def agregar_computadora(self,computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadora_str = ''
        for computadora in self._computadoras:
            computadora_str += computadora.__str__()

        return '''
            Orden: {}
            Computadoras: {}
        '''.format(self._ide_ordenes, computadora_str)
