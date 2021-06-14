from dispositivo_entrada import DisposistivoEntrada

class Raton(DisposistivoEntrada):

    contado_ratones = 0

    def __init__(self, marca, tipo_entrada):
        Raton.contado_ratones += 1
        self._id_raton = Raton.contado_ratones
        super(Raton, self).__init__(marca, tipo_entrada)

    def __str__(self):
        return 'ID: {}, Marca: {}, Tipo_entrada: {}'.format(self._id_raton, self._marca, self._tipo_entrada)


if __name__ == '__main__':
    raton1 = Raton('HP', 'USB')
    print(raton1)
