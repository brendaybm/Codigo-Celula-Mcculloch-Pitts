class CelulaMcCullochPitts:
    def __init__(self, n_entradas, funcion_activacion):
        self.n_entradas = n_entradas
        self.funcion_activacion = funcion_activacion
        self.umbral = 0
        self.pesos = [0] * n_entradas

    def prediccion(self, entradas):
        # calculamos la suma ponderada de las entradas
        suma = 0
        for i in range(self.n_entradas):
            suma += entradas[i] * self.pesos[i]
        # aplicamos la función de activación y devolvemos el resultado
        return self.funcion_activacion(suma - self.umbral)

or_celula = CelulaMcCullochPitts(2, lambda x: 1 if x >= 1 else 0)
or_celula.prediccion([0, 1])
