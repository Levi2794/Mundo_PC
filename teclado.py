from dispositivo_entrada import DisposistivoEntrada

class Teclado(DisposistivoEntrada):
    contador_teclado = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclado += 1
        self._id_teclado = Teclado.contador_teclado
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return 'Id: {}, Marca: {}, Tipo Entrada: {}'.format(self._id_teclado, self._marca, self._tipo_entrada)

if __name__ == '__main__':
    teclado = Teclado('Logitech', 'USB')
    print(teclado)
    teclado_2 = Teclado('Samsung', 'Wi-Fi')
    print(teclado_2)

