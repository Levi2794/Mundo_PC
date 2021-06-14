class Monitor:
    contador_monitor = 0

    def __init__(self, marca, tamaño):
        Monitor.contador_monitor += 1
        self._id_monitor = Monitor.contador_monitor
        self._marca = marca
        self._tamaño = tamaño

    def __str__(self):
        return 'Id: {}, Marca: {}, Tamaño: {}'.format(self._id_monitor, self._marca, self._tamaño)

if __name__ == '__main__':
    monitor = Monitor('Samsung', 22)
    print(monitor)
    monitor_2 = Monitor('Aser', 27)
    print(monitor_2)